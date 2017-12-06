import React, {Component} from 'react';

class ScoreTable extends Component {
  render() {
    return this.props.scores.map((tone, idx) => {
      return (<div key={idx}>
        <div className="tone_name">
          {tone.tone_name}
        </div>
        <div className="tone_score">
          {`${tone.score}`.substring(0, 9)}
        </div>
      </div>)
    });
  }
}

export default ScoreTable;
