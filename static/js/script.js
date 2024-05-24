document.addEventListener("DOMContentLoaded", () => {
  const quizForm = document.getElementById("quiz-form");
  const resultContainer = document.getElementById("result-container");

  if (quizForm) {
    quizForm.addEventListener("submit", function (event) {
      event.preventDefault();
      const formData = new FormData(quizForm);
      fetch("/submit", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.next_question) {
            updateQuestion(data.next_question, data.q_num);
          } else {
            showResult(data.score, data.message);
          }
        });
    });
  }

  function updateQuestion(question, q_num) {
    document.getElementById("question-num").textContent = `Question ${q_num}`;
    document.getElementById("question-text").innerHTML = question.question;
    const optionsContainer = document.getElementById("options-container");
    optionsContainer.innerHTML = "";
    question.options.forEach((option) => {
      const optionElement = document.createElement("li");
      optionElement.innerHTML = `<input type="radio" name="option" value="${option}" required> ${option}`;
      optionsContainer.appendChild(optionElement);
    });
  }

  function showResult(score, message) {
    resultContainer.innerHTML = `
            <h2>Your score: ${score}/10</h2>
            <p>${message}</p>
            <a href="/">Play Again</a>
        `;
    quizForm.style.display = "none";
  }
});
