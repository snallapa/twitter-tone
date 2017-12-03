import React, { Component } from 'react';
import ScoreTable from './ScoreTable';

class Overall extends Component {
  render() {
    if (this.props.overall.length === 0) {
      return false;
    }
    return (
      <div>
        <h1>Overall</h1>
        <div className="overall__score">
            <ScoreTable scores={this.props.overall} />
        </div>
      </div>
    );
  }
}

export default Overall;
