import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">OctoFit Tracker</Link>
          <button 
            className="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav" 
            aria-controls="navbarNav" 
            aria-expanded="false" 
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container-fluid">
        <Routes>
          <Route path="/" element={
            <div className="container mt-4">
              <h1 className="mb-3">Welcome to OctoFit Tracker</h1>
              <p className="lead mb-4">Track your fitness journey with your team!</p>
              <div className="row mt-4">
                <div className="col-md-4 mb-4">
                  <div className="card h-100">
                    <div className="card-body d-flex flex-column">
                      <h5 className="card-title">
                        <i className="bi bi-activity"></i> Track Activities
                      </h5>
                      <p className="card-text flex-grow-1">Log your workouts and monitor your progress.</p>
                      <Link to="/activities" className="btn btn-primary mt-auto">View Activities</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 mb-4">
                  <div className="card h-100">
                    <div className="card-body d-flex flex-column">
                      <h5 className="card-title">
                        <i className="bi bi-people-fill"></i> Join Teams
                      </h5>
                      <p className="card-text flex-grow-1">Compete with your teammates and stay motivated.</p>
                      <Link to="/teams" className="btn btn-primary mt-auto">View Teams</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 mb-4">
                  <div className="card h-100">
                    <div className="card-body d-flex flex-column">
                      <h5 className="card-title">
                        <i className="bi bi-trophy"></i> Check Leaderboard
                      </h5>
                      <p className="card-text flex-grow-1">See how you rank against others.</p>
                      <Link to="/leaderboard" className="btn btn-primary mt-auto">View Leaderboard</Link>
                    </div>
                  </div>
                </div>
              </div>
              <div className="row mt-3">
                <div className="col-md-6 mb-4">
                  <div className="card h-100">
                    <div className="card-body d-flex flex-column">
                      <h5 className="card-title">
                        <i className="bi bi-people"></i> Manage Users
                      </h5>
                      <p className="card-text flex-grow-1">View all registered users and their profiles.</p>
                      <Link to="/users" className="btn btn-primary mt-auto">View Users</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-6 mb-4">
                  <div className="card h-100">
                    <div className="card-body d-flex flex-column">
                      <h5 className="card-title">
                        <i className="bi bi-lightning-charge"></i> Workout Suggestions
                      </h5>
                      <p className="card-text flex-grow-1">Get personalized workout recommendations.</p>
                      <Link to="/workouts" className="btn btn-primary mt-auto">View Workouts</Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
