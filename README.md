# React Web App with Flask Backend for PyTorch Model

### FullStack AI Series- Part 2 (CellStrat AI Lab)

This repository contains the code for React Web App with Flask Backend for PyTorch Model Session and is a part of the Full stack AI Love Coding Series at CellStrat AI Lab.

In this part, the BERT model that was trained in part 1 is wrapped around a React Frontend and Flask Backend for inference.

Checkout the code from the other parts here:

- [Part 1](https://github.com/theneuralbeing/bert-finetuning-webinar)
- [Part 3](https://github.com/theneuralbeing/bert-deployment-aws)

#### Usage

1. Clone the repository

```bash
git clone https://github.com/theneuralbeing/bert-web-app.git
```

2. Download the trained sentiment analysis model from [here](https://gradient-fire.s3.amazonaws.com/inference.pth)
3. Download the bert-base-uncased model from [here](https://gradient-fire.s3.amazonaws.com/bert-base-uncased.rar) and then unzip the archive
4. Move both the downloaded files to [backend](backend) directory

5. Create your react app as shown in the coding session. The react source code can be found in [bert-app](bert-app)

Note: You cannot run the react application from this repository.

6. Start your react app with `npm start` in the terminal.
7. Open another terminal and `cd` to [backend](backend) directory and start the flask server using this command `python app.py`
8. Now you can play around with your sentiment analysis web app.
