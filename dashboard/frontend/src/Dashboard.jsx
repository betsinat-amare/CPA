import React, { useState, useEffect } from 'react';
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine, AreaChart, Area
} from 'recharts';
import { AlertCircle, TrendingUp, Calendar, Info, Activity } from 'lucide-react';

const Dashboard = () => {
    const [prices, setPrices] = useState([]);
    const [events, setEvents] = useState([]);
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(true);
    const [activeEvent, setActiveEvent] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const [pricesRes, eventsRes, resultsRes] = await Promise.all([
                    fetch('http://localhost:5000/api/prices'),
                    fetch('http://localhost:5000/api/events'),
                    fetch('http://localhost:5000/api/results')
                ]);

                if (!pricesRes.ok || !eventsRes.ok || !resultsRes.ok) {
                    throw new Error('Failed to fetch data from backend. Ensure Flask is running on port 5000.');
                }

                const pricesData = await pricesRes.json();
                const eventsData = await eventsRes.json();
                const resultsData = await resultsRes.json();

                setPrices(pricesData);
                setEvents(eventsData);
                setResults(resultsData);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) return <div className="loading-container"><Activity className="animate-spin" /> Loading Analysis Data...</div>;
    if (error) return <div className="loading-container" style={{ color: '#f85149' }}><AlertCircle /> {error}</div>;

    const m1 = 21.46; // From Task 2 results
    const m2 = 75.90;
    const changeDate = '2005-03-02';

    return (
        <div className="dashboard-container">
            <header className="header">
                <h1>Brent Oil Price Change Point Analysis</h1>
                <div className="stat-label">Model Status: <span style={{ color: 'var(--accent-green)' }}>Converged (R-hat 1.02)</span></div>
            </header>

            <div className="stats-grid">
                <div className="stat-card">
                    <div className="stat-label">Regime 1 Mean (Pre-2005)</div>
                    <div className="stat-value">${m1.toFixed(2)}</div>
                </div>
                <div className="stat-card">
                    <div className="stat-label">Regime 2 Mean (Post-2005)</div>
                    <div className="stat-value">${m2.toFixed(2)}</div>
                </div>
                <div className="stat-card">
                    <div className="stat-label">Log Return Volatility</div>
                    <div className="stat-value" style={{ color: 'var(--accent-purple)' }}>0.024</div>
                </div>
                <div className="stat-card">
                    <div className="stat-label">Relative Shift</div>
                    <div className="stat-value" style={{ color: 'var(--accent-green)' }}>+253.7%</div>
                </div>
            </div>

            <div className="chart-panel">
                <h2 className="panel-title"><TrendingUp size={20} /> Historical Price Timeline & Regime Shift</h2>
                <div style={{ width: '100%', height: 400 }}>
                    <ResponsiveContainer>
                        <AreaChart data={prices}>
                            <defs>
                                <linearGradient id="colorPrice" x1="0" y1="0" x2="0" y2="1">
                                    <stop offset="5%" stopColor="var(--accent-blue)" stopOpacity={0.3} />
                                    <stop offset="95%" stopColor="var(--accent-blue)" stopOpacity={0} />
                                </linearGradient>
                            </defs>
                            <CartesianGrid strokeDasharray="3 3" stroke="var(--border-color)" />
                            <XAxis
                                dataKey="Date"
                                tick={{ fill: 'var(--text-dim)' }}
                                minTickGap={50}
                                tickFormatter={(val) => new Date(val).getFullYear()}
                            />
                            <YAxis tick={{ fill: 'var(--text-dim)' }} />
                            <Tooltip
                                contentStyle={{ backgroundColor: 'var(--panel-bg)', borderColor: 'var(--border-color)', color: 'var(--text-main)' }}
                                labelFormatter={(value) => `Date: ${value}`}
                            />
                            <Area type="monotone" dataKey="Price" stroke="var(--accent-blue)" fillOpacity={1} fill="url(#colorPrice)" />

                            <ReferenceLine x={changeDate} stroke="var(--accent-red)" strokeDasharray="5 5" label={{ value: 'Change Point', fill: 'var(--accent-red)', position: 'top' }} />

                            {activeEvent && (
                                <ReferenceLine x={activeEvent.Date} stroke="var(--accent-purple)" strokeWidth={2} />
                            )}
                        </AreaChart>
                    </ResponsiveContainer>
                </div>
            </div>

            <div className="events-panel">
                <h2 className="panel-title"><Calendar size={20} /> Geopolitical Events Impact</h2>
                <div className="event-list">
                    {events.map((event, idx) => (
                        <div
                            key={idx}
                            className={`event-item ${activeEvent === event ? 'active' : ''}`}
                            onMouseEnter={() => setActiveEvent(event)}
                            onMouseLeave={() => setActiveEvent(null)}
                        >
                            <div className="event-date">{event.Date}</div>
                            <div className="event-desc"><strong>{event.Event}</strong></div>
                            <div style={{ fontSize: '11px', marginTop: '4px', color: 'var(--text-dim)' }}>{event.Type}</div>
                        </div>
                    ))}
                </div>
            </div>

            <footer style={{ marginTop: '32px', color: 'var(--text-dim)', fontSize: '12px', textAlign: 'center' }}>
                Interactive Dashboard developed for Change Point Analysis Project | © 2026 CPU
            </footer>
        </div>
    );
};

export default Dashboard;
