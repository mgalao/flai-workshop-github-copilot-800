import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        console.log('Workouts response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts processed data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
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
        <h3 className="mt-3 text-muted">Loading workouts...</h3>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error Loading Workouts</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  const getDifficultyBadge = (level) => {
    const badges = {
      'Beginner': 'bg-success',
      'Intermediate': 'bg-warning text-dark',
      'Advanced': 'bg-danger'
    };
    return badges[level] || 'bg-secondary';
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-4">
        <i className="bi bi-lightning-charge"></i> Workout Suggestions
      </h2>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{workout.title}</h5>
                  <p className="card-text">{workout.description}</p>
                  <ul className="list-group list-group-flush mt-3">
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Category:</strong>
                      <span className="badge bg-info text-dark">{workout.category}</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Difficulty:</strong>
                      <span className={`badge ${getDifficultyBadge(workout.difficulty_level)}`}>
                        {workout.difficulty_level}
                      </span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Duration:</strong>
                      <span className="badge bg-primary">{workout.duration} minutes</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Equipment:</strong>
                      <span className="badge bg-secondary">{workout.equipment_needed || 'None'}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info" role="alert">
              No workouts found
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
