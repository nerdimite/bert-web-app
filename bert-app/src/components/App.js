import React from "react";
import ReviewBox from "./ReviewBox";
import Output from "./Output";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.output = React.createRef();
  }

  onFormSubmit = async review => {
    const response = await fetch("/pred", {
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      method: "POST",
      body: JSON.stringify({
        body: review
      })
    });
    const prediction = await response.text();
    console.log(prediction);
    this.output.current.onGettingPred(prediction);
  };

  render() {
    return (
      <div className="ui container">
        <div className="sixteen wide column" style={{ marginTop: "20px" }}>
          <h1> BERT Sentiment Analysis </h1>
        </div>
        <div className="sixteen wide column" style={{ marginTop: "20px" }}>
          <ReviewBox onFormSubmit={this.onFormSubmit} />
        </div>
        <div className="sixteen wide column" style={{ marginTop: "20px" }}>
          <Output ref={this.output} />
        </div>
      </div>
    );
  }
}
export default App;
