import React, {Component} from 'react';
import './App.css';
import Overall from './Overall';
import Individual from './Individual';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      value: "",
      overall: [],
      tweets: [],
      loading: false
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    this.setState({
      ...this.state,
      loading: true
    });

    fetch(`/tone/${this.state.value.replace("#", "")}`).then((res) => {
      res.json().then((data) => {
        this.setState({value: this.state.value, overall: data.overall, tweets: data.individual, loading: false});
      });
    });
  }

  render() {
    return (<div className="App">
      <div className="header-text">Twitter Tone Analyzer</div>
      <form onSubmit={this.handleSubmit}>
        <input className="twitter-search" type="text" value={this.state.value} onChange={this.handleChange} placeholder="Search"/>
        <button className="twitter-submit" type="submit">
          Submit
        </button>
      </form>
      {this.state.loading && this.renderLoading()}
      <Overall overall={this.state.overall}/>
      <Individual tweets={this.state.tweets}/>
    </div>);
  }

  renderLoading() {
    return (<div className="loading">
      Loading...
    </div>);
  }
}

export default App;
