import React, { Component } from "react";
import BookPage from "./BookPage";
import RoomPage from "./RoomPage";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class homepage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <p>This is the home page</p>
          </Route>
          <Route path="/BookRoom" component={RoomPage} />
          <Route path="/BrowseBooks" component={BookPage} />
        </Switch>
      </Router>
    );
  }
}