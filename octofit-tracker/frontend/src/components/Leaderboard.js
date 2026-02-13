import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Leaderboard API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        console.log('Leaderboard response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard processed data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-4 text-center">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <h3 className="mt-3 text-muted">Loading leaderboard...</h3>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error Loading Leaderboard</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <h2 className="mb-4">
        <i className="bi bi-trophy"></i> Leaderboard
      </h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Team</th>
              <th>Total Points</th>
              <th>Period</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => {
                const rank = index + 1;
                const rankClass = rank <= 3 ? `rank-badge rank-${rank}` : '';
                return (
                  <tr key={entry.id}>
                    <td>
                      {rank <= 3 ? (
                        <span className={rankClass}>{rank}</span>
                      ) : (
                        <span className="badge bg-secondary">{rank}</span>
                      )}
                    </td>
                    <td><strong>{entry.user_name || entry.user}</strong></td>
                    <td>
                      <span className="badge bg-primary">{entry.team_name || entry.team}</span>
                    </td>
                    <td>
                      <span className="badge bg-warning text-dark">{entry.total_points} pts</span>
                    </td>
                    <td>{entry.period}</td>
                  </tr>
                );
              })
            ) : (
              <tr>
                <td colSpan="5" className="text-center text-muted">
                  <p className="my-3">No leaderboard data found</p>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
