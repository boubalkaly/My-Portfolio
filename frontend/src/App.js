import './styles/App.css';
import Header from './components/Header.js'
import Home from './components/Home.js'
import Projects from './components/Projects.js'

function App() {
  return (
    <div className="App">
      <Header />
      <Home />
      <Projects/>

    </div>
  );
}

export default App;
