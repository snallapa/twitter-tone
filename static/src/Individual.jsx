import React, { Component } from 'react';
import ScoreTable from './ScoreTable';

class Individual extends Component {
  render() {
    if (this.props.tweets.length === 0) {
        return false;
    }
    return (
      <div className="individual-section">
        <h1>Individual Tweets</h1>
        {this.renderTweets()}
      </div>
    );
  }

  renderTweets() {
      return this.props.tweets.map((tweet, idx) => {
          return (
              <div key={idx} className="individual">
                <a className="tweet" href={`https://twitter.com/statuses/${tweet.tweet_id}`} target="_blank">
                    <img className="tweet__image" src={tweet.userImage.replace("normal", "bigger")} alt="twitter profile"/>
                    <div className="tweet__text">
                        <div>
                            <span className="user"> {tweet.user}</span> <span className="screen-name">{`@${tweet.screen_name}`} </span>
                        </div>
                        <div className="tweet__text-full">
                            {tweet.text}
                        </div>
                    </div>
                </a>
                <ScoreTable scores={tweet.tones} />
              </div>
          )
      });
  }
}

export default Individual;
