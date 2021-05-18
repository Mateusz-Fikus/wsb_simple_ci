import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  // Link
} from "react-router-dom";
import { Navbar } from './components/Navbar/Navbar'
import {Home } from "./components/Home/Home"
import { Footer } from "./components/Footer/Footer"

const App: React.FC = () => {
  return (
    <div className="App">
      <Router>
        <Navbar/>
          <Switch>
              <Route exact path="/">
                <Home/>
              </Route>
              <Route path="/login">
                <div>login</div>
              </Route>
          </Switch>
        <Footer/>
      </Router>
    </div>
  );
}

export default App;
