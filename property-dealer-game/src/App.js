// import logo from './logo.svg';
// import './App.css';
import './styles/Game.css'

function App() {
  return (
    <div className="App">
      <title>Property Dealer</title>

      <body className="">
        <nav>
          <h1>Nav Bar</h1>
          {/* <p>Nav Bar p</p> */}
        </nav>

        <main>

          <div className="opp-player-container">
            <div className="opp-player-2-container">
              <div class="player-2-info-container">
                <h3>Player 2 Info</h3>
              </div>
              
              <div className="player-2-card-container">
                Player Card
              </div>
            </div>

            <div className="opp-player-3-container">
              <div class="player-3-info-container">
                <h3>Player 3 Info</h3>
              </div>

              <div className="player-3-card-container">
                Player Card
              </div>
            </div>

            <div className="opp-player-4-container">
              <div class="player-4-info-container">
                <h3>Player 4 Info</h3>
              </div>

              <div className="player-4-card-container">
                Player Card
              </div>
            </div>
          </div>

          <div className="main-player-container">
            <div className="game-interaction-container">
              Game State Info & Player Profile
            </div>
            <div className="main-player-card-container">
              Player's Cards
            </div>
            <div className="main-player-hand-container">
              Player's Hand
            </div>
          </div>
        </main>
      </body>
    </div>
  );
}

export default App;
