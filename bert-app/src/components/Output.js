import React from "react";

class Output extends React.Component {
  state = { output: "Waiting", icon: "ellipsis horizontal" };

  onInputChange = event => {
    this.setState({ text: event.target.value });
  };

  onGettingPred = res => {
    if (res === "1") {
      this.setState({ output: "Positive Review", icon: "check" });
    } else if (res === "0") {
      this.setState({ output: "Negative Review", icon: "x icon" });
    } else {
      this.setState({
        output: "Error: Check console for details",
        icon: "exclamation"
      });
    }
    console.log(this.state.output);
  };

  render() {
    return (
      <div className="ui segment">
        <i className={`${this.state.icon} large icon`} />
        {this.state.output}
      </div>
    );
  }
}
export default Output;
