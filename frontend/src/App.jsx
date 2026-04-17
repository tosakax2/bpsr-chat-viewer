import React, { useState, useEffect, useRef } from 'react';
import { Settings, Wifi, WifiOff, MessageSquare, Filter, Trash2, Bell, BellOff, ExternalLink, Volume2 } from 'lucide-react';

const CHANNEL_CONFIG = {
  world: { label: 'World', color: '#a855f7', bg: 'rgba(168, 85, 247, 0.15)' },
  guild: { label: 'Guild', color: '#84cc16', bg: 'rgba(132, 204, 22, 0.15)' },
  scene: { label: 'Channel', color: '#cbd5e1', bg: 'rgba(203, 213, 225, 0.15)' }, // Softened white
  party: { label: 'Team', color: '#06b6d4', bg: 'rgba(6, 182, 212, 0.15)' },
  system: { label: 'System', color: '#f59e0b', bg: 'rgba(245, 158, 11, 0.15)' },
};

function App() {
  // Detect if we are in pop-out mode for a specific channel
  const searchParams = new URL(window.location.href).searchParams;
  const channelParam = searchParams.get('channel');
  const isPopout = !!channelParam && !!CHANNEL_CONFIG[channelParam];

  const [messages, setMessages] = useState([]);
  const [status, setStatus] = useState('connecting');
  const [showSettings, setShowSettings] = useState(false);
  const [showFilters, setShowFilters] = useState(false);
  const [volume, setVolume] = useState(() => {
    const saved = localStorage.getItem('bpsr_volume');
    return saved ? parseFloat(saved) : 0.4; // Default to 40%
  });
  
  const [filters, setFilters] = useState(() => {
    if (isPopout) {
      const initialFilters = { world: false, scene: false, guild: false, party: false, system: false };
      initialFilters[channelParam] = true;
      return initialFilters;
    }
    return { world: true, scene: true, guild: true, party: true, system: true };
  });
  
  const [useSound, setUseSound] = useState(true);
  const useSoundRef = useRef(useSound);
  const volumeRef = useRef(volume);
  const scrollRef = useRef(null);
  const ws = useRef(null);
  const reconnectTimeout = useRef(null);

  // Sync sound setting to ref to avoid stale closures in WS handler
  useEffect(() => {
    useSoundRef.current = useSound;
  }, [useSound]);

  // Sync volume to ref and localStorage
  useEffect(() => {
    volumeRef.current = volume;
    localStorage.setItem('bpsr_volume', volume.toString());
  }, [volume]);

  useEffect(() => {
    connect();
    return () => {
      if (ws.current) {
        ws.current.onclose = null; // Prevent reconnection on manual close
        ws.current.close();
      }
      if (reconnectTimeout.current) clearTimeout(reconnectTimeout.current);
    };
  }, []);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  const connect = () => {
    // Clear any existing connection
    if (ws.current) {
      ws.current.onclose = null;
      ws.current.close();
    }
    if (reconnectTimeout.current) clearTimeout(reconnectTimeout.current);

    setStatus('connecting');
    console.log('Attempting to connect to WebSocket...');
    
    try {
      ws.current = new WebSocket('ws://localhost:8000/ws');

      ws.current.onopen = () => {
        setStatus('connected');
        console.log('Connected to backend');
      };

      ws.current.onmessage = (event) => {
        const data = JSON.parse(event.data);
        // Only trigger message addition if it's either not popout mode or matches the channel
        if (!isPopout || data.channel === channelParam) {
          setMessages((prev) => [...prev.slice(-199), { ...data, id: Date.now() + Math.random() }]);
          playNotification(data.channel);
        }
      };

      ws.current.onclose = () => {
        setStatus('disconnected');
        console.log('WebSocket disconnected. Retrying in 3s...');
        reconnectTimeout.current = setTimeout(connect, 3000);
      };

      ws.current.onerror = (err) => {
        console.error('WebSocket Error:', err);
      };
    } catch (err) {
      console.error('Failed to create WebSocket:', err);
      reconnectTimeout.current = setTimeout(connect, 3000);
    }
  };

  const openPopout = (channel) => {
    // Check if running in pywebview standalone environment
    if (window.pywebview && window.pywebview.api && window.pywebview.api.open_popout) {
      window.pywebview.api.open_popout(channel);
    } else {
      // Fallback to browser window.open if pywebview is not available
      const url = `${window.location.origin}${window.location.pathname}?channel=${channel}`;
      window.open(url, `bpsr_chat_${channel}`, 'width=450,height=700,menubar=no,toolbar=no,location=no,status=no');
    }
  };

  const playNotification = (channel) => {
    if (!useSoundRef.current) return;
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      const ctx = new AudioContext();
      
      const playNote = (freq, startTime, duration) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, startTime);
        
        gain.gain.setValueAtTime(0, startTime);
        gain.gain.linearRampToValueAtTime(volumeRef.current, startTime + 0.01);
        gain.gain.exponentialRampToValueAtTime(0.01, startTime + duration);
        
        const panner = ctx.createStereoPanner();
        panner.pan.value = 0; // Center the sound explicitly
        
        osc.connect(gain);
        gain.connect(panner);
        panner.connect(ctx.destination);
        osc.start(startTime);
        osc.stop(startTime + duration);
      };

      const now = ctx.currentTime;
      // Define different melodies for each channel
      switch (channel) {
        case 'world':
          playNote(880, now, 0.3);        // A5
          playNote(1108.73, now + 0.05, 0.4); // C#6 (Bright Major 3rd)
          break;
        case 'guild':
          playNote(659.25, now, 0.3);      // E5
          playNote(783.99, now + 0.05, 0.4); // G5 (Stable Minor 3rd)
          break;
        case 'scene':
          playNote(1046.50, now, 0.15);    // C6 (Short High Ping)
          break;
        case 'party':
          playNote(783.99, now, 0.15);     // G5
          playNote(987.77, now + 0.1, 0.15); // B5
          playNote(1174.66, now + 0.2, 0.3); // D6 (Upward Arpeggio)
          break;
        case 'system':
          playNote(349.23, now, 0.5);      // F4 (Muted low note)
          break;
        default:
          playNote(880, now, 0.3);
          playNote(1108.73, now + 0.05, 0.4);
      }
    } catch (e) {
      console.error('Audio play failed:', e);
    }
  };

  const clearMessages = () => setMessages([]);

  const filteredMessages = messages.filter(m => filters[m.channel]);

  const toggleFilters = () => {
    setShowFilters(!showFilters);
    if (showSettings) setShowSettings(false);
  };

  const toggleSettings = () => {
    setShowSettings(!showSettings);
    if (showFilters) setShowFilters(false);
  };

  const toggleFilter = (channel) => {
    setFilters(prev => ({ ...prev, [channel]: !prev[channel] }));
  };

  return (
    <div className={`app-container ${isPopout ? 'popout-mode' : ''}`}>

      {/* Unified App Header */}
      <header 
        className="app-header"
        style={{ '--channel-color': isPopout ? CHANNEL_CONFIG[channelParam].color : '#60a5fa' }}
      >
        <div className="header-left">
          <div className={`status-dot ${status}`} title={`Status: ${status}`} />
          <span className="channel-label">
            {isPopout ? CHANNEL_CONFIG[channelParam].label : 'BPSR Chat Viewer'}
          </span>
        </div>
        {!isPopout && (
          <div className="controls">
            
            {/* Filter Panel */}
            <div className="settings-wrapper">
              <button 
                onClick={toggleFilters} 
                className={`icon-button ${showFilters ? 'active' : ''}`} 
                title="Channel Filters"
              >
                <Filter size={18} />
              </button>
              
              {showFilters && (
                <div className="filters-panel glass-panel">
                  <div className="panel-title">Visible Channels</div>
                  <div className="filters-list">
                    {Object.entries(CHANNEL_CONFIG).map(([id, config]) => (
                      <div key={id} className="filter-row">
                        <label className={`filter-item ${filters[id] ? 'active' : ''}`} style={{ '--channel-color': config.color }}>
                          <input
                            type="checkbox"
                            checked={filters[id]}
                            onChange={() => toggleFilter(id)}
                          />
                          <div className="channel-indicator" />
                          <span>{config.label}</span>
                        </label>
                        <button 
                          className="popout-inline-btn" 
                          onClick={() => openPopout(id)}
                          title={`Open ${config.label} in new window`}
                        >
                          <ExternalLink size={14} />
                        </button>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Settings Panel */}
            <div className="settings-wrapper">
              <button 
                onClick={toggleSettings} 
                className={`icon-button ${showSettings ? 'active' : ''}`} 
                title="Status & Settings"
              >
                <Settings size={18} />
              </button>
              
              {showSettings && (
                <div className="settings-panel glass-panel">
                  <div className="settings-group">
                    <div className="settings-item">
                      <div className="settings-label">
                        <Bell size={14} />
                        <span>Sound: {useSound ? 'ON' : 'OFF'}</span>
                      </div>
                      <button 
                        onClick={() => setUseSound(!useSound)} 
                        className={`toggle-btn ${useSound ? 'active' : ''}`}
                      >
                        {useSound ? 'Toggle' : 'Toggle'}
                      </button>
                    </div>

                    <div className="settings-item">
                      <div className="settings-label">
                        <Volume2 size={14} />
                        <span>Volume: {Math.round(volume * 100)}%</span>
                      </div>
                      <input 
                        type="range" 
                        min="0" 
                        max="1" 
                        step="0.05" 
                        value={volume} 
                        onChange={(e) => setVolume(parseFloat(e.target.value))}
                      />
                    </div>

                    <div className="settings-divider" />

                    <button onClick={clearMessages} className="action-btn-danger">
                      <Trash2 size={14} />
                      <span>Clear History</span>
                    </button>
                  </div>
                  
                  <div className="settings-footer">
                    <span>v0.1.5 - Unified UI</span>
                  </div>
                </div>
              )}
            </div>
          </div>
        )}
      </header>


      {/* Chat Messages */}
      <main className="chat-area" ref={scrollRef}>
        <div className="message-list">
          {filteredMessages.length === 0 ? (
            <div className="empty-state">No messages yet. Start chatting in-game.</div>
          ) : (
            filteredMessages.map((msg) => (
              <div key={msg.id} className="message-item animate-in" style={{ '--channel-color': CHANNEL_CONFIG[msg.channel]?.color }}>
                <div className="message-header">
                  <span className="channel-tag" style={{ color: CHANNEL_CONFIG[msg.channel]?.color, backgroundColor: CHANNEL_CONFIG[msg.channel]?.bg }}>
                    {CHANNEL_CONFIG[msg.channel]?.label}
                  </span>
                  <span className="sender">{msg.sender}</span>
                  <span className="time">{new Date(msg.timestamp * 1000).toLocaleTimeString()}</span>
                </div>
                <div className="message-content">{msg.content}</div>
              </div>
            ))
          )}
        </div>
      </main>

    </div>
  );
}

export default App;
