const question = document.getElementById('question');
const choices = Array.from(document.getElementsByClassName("choice-text"));
const progressText = document.getElementById('progressText');
const scoreText = document.getElementById('score');
const progressBarFull = document.getElementById('progressBarFull');

// const loader = document.getElementById('loader')
const game = document.getElementById('game');


let currentQuestion = {};
let acceptingAnswes = false;
let score = 0;
let questionCounter = 0;
let availableQuestions = [];

let questions = []; //voir json

//fetch question from .json:

fetch(
    //"questions.json"
    "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"
    // "https://www.khanacademy.org/api/v1/exercises"
    )
.then(res =>{
    return res.json();
})
  .then(loadedQuestions => {
      console.log(loadedQuestions.results);

      questions = loadedQuestions.results.map(loadedQuestion => {
          const formattedQuestion = {
             question: loadedQuestion.question
          };

          const answerChoices = [...loadedQuestion.incorrect_answers];
          formattedQuestion.answer = Math.floor(Math.random() * 3) + 1;
          answerChoices.slice(
              formattedQuestion.answer - 1,
              0,
              loadedQuestion.correct_answer
          );

          answerChoices.forEach((choice, index) =>{
              formattedQuestion["choice" + (index +1)] = choice;
          });
          return formattedQuestion;
      });

      
       
      //questions = loadedQuestions;
      startGame();
  })
    .catch(err => {
         console.log(err);
    });


//CONSTANTS
const CORRECT_BONUS = 10;
const MAX_QUESTIONS = 3;

startGame = () =>{
    questionCounter = 0;
    score = 0;
    availableQuestions = [...questions]; //copy all the qst from questions array to the availableQuestions one
    
    getNewQuestions();

    //remove the loading and turn the game:
    game.classList.remove("hidden");
    loader.classList.add("hidden");
};


getNewQuestions = () =>{
     
    if(availableQuestions.length ===0 || questionCounter >= MAX_QUESTIONS){

        //save the user score:
        localStorage.setItem("mostRecentScore", score);
        //go to ebd of the page:

        return window.location.assign('end');


    }

    questionCounter++;
    progressText.innerText = ` Question ${questionCounter}/${MAX_QUESTIONS}`;
 
    //UPDATE THE PROGRESS BAR:(on prend pourcentage de chq qstn vrai)

   progressBarFull.style.width = `${(questionCounter / MAX_QUESTIONS) * 100}%`; //val en % ``

     const questionIndex = Math.floor(Math.random() * availableQuestions.length);
     currentQuestion = availableQuestions[questionIndex];
     question.innerText = currentQuestion.question;

     choices.forEach(choice =>{
          const number = choice.dataset['number']; //aller au data-nmbr ds game.html
          choice.innerText = currentQuestion['choice' + number]; // remplaer choice i par sa val i qui est ds tab

     });

     availableQuestions.splice(questionIndex, 1); //so as to get red from the question that we use before

     acceptingAnswes= true;
};

choices.forEach(choice =>{
    choice.addEventListener('click', e => {
           if(!acceptingAnswes) return;

           acceptingAnswes = false;
           const selectedChoice = e.target;
           const selectedAnswer = selectedChoice.dataset['number'];

            const classToApply = 
            selectedAnswer == currentQuestion.answer ? 'correct' : 'incorrect';
           
               //increment the score if the correct answer:
                  if(classToApply === 'correct'){
                      incrementScore(CORRECT_BONUS);
                  }  

            //add the class:
            selectedChoice.parentElement.classList.add(classToApply);

            setTimeout(() =>{
                //remove that class after his work:
                selectedChoice.parentElement.classList.remove(classToApply);
                getNewQuestions();
            },1000); //how long to do the main setTimeout

        

          
           
    });
});

incrementScore = num => {
    score +=num;
    scoreText.innerText = score;  
}

//startGame();
