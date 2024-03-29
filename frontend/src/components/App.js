import React, { Component } from "react";
import { render } from "react-dom"
import RoomPage from "./RoomPage";
import BookPage from "./BookPage";
import homepage from "./homepage";


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
        <div> 
            <homepage />
            <BookPage />
            <RoomPage />
            
        </div>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);