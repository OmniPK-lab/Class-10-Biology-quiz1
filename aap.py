<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CBSE Class 10 Biology Master Quiz</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- MathJax for rendering equations cleanly if needed -->
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(229, 231, 235, 0.8);
        }
        .option-btn {
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }
    </style>
</head>
<body class="bg-slate-900 text-slate-800 min-h-screen flex flex-col justify-between selection:bg-emerald-500 selection:text-white">

    <!-- Top Navigation Header -->
    <header class="w-full bg-slate-900/80 border-b border-slate-800 sticky top-0 z-50 backdrop-blur-md">
        <div class="max-w-5xl mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="bg-gradient-to-tr from-emerald-500 to-teal-400 p-2.5 rounded-xl shadow-lg shadow-emerald-500/20">
                    <i class="fa-solid fa-dna text-white text-xl"></i>
                </div>
                <div>
                    <h1 class="text-white font-bold text-lg leading-tight">Class 10 Biology</h1>
                    <p class="text-xs text-slate-400 font-medium">CBSE Board Exam Practice</p>
                </div>
            </div>
            
            <!-- Overall Stats badge in header -->
            <div id="header-timer" class="hidden items-center space-x-2 bg-slate-800 border border-slate-700/60 px-4 py-1.5 rounded-full">
                <i class="fa-regular fa-clock text-amber-400 text-sm"></i>
                <span id="timer-text" class="text-slate-200 font-mono font-semibold text-sm">00:00</span>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-grow flex items-center justify-center p-4 sm:p-6 my-auto">
        
        <!-- 1. LANDING / HERO SCREEN -->
        <div id="welcome-screen" class="max-w-3xl w-full">
            <div class="glass-card rounded-3xl p-6 sm:p-10 shadow-2xl relative overflow-hidden">
                <div class="absolute -top-12 -right-12 w-40 h-40 bg-emerald-500/10 rounded-full blur-2xl pointer-events-none"></div>
                <div class="absolute -bottom-12 -left-12 w-40 h-40 bg-teal-500/10 rounded-full blur-2xl pointer-events-none"></div>

                <div class="text-center max-w-xl mx-auto space-y-4">
                    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 border border-emerald-200">
                        <i class="fa-solid fa-sparkles text-xs"></i> Class X Science Practice
                    </span>
                    <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
                        Biology Mastery Quiz
                    </h2>
                    <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
                        Comprehensive interactive quiz tailored for CBSE Class 10 covering all key concepts, diagrams, assertions, and board exam problems.
                    </p>
                </div>

                <!-- Syllabus Grid -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 my-8">
                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-100 text-center">
                        <div class="w-8 h-8 mx-auto mb-2 rounded-lg bg-emerald-500/10 text-emerald-600 flex items-center justify-center">
                            <i class="fa-solid fa-heart-pulse text-sm"></i>
                        </div>
                        <h3 class="text-xs font-bold text-slate-800">Life Processes</h3>
                        <p class="text-[10px] text-slate-500 mt-0.5">Nutrition, Respiration, Excretion</p>
                    </div>

                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-100 text-center">
                        <div class="w-8 h-8 mx-auto mb-2 rounded-lg bg-cyan-500/10 text-cyan-600 flex items-center justify-center">
                            <i class="fa-solid fa-brain text-sm"></i>
                        </div>
                        <h3 class="text-xs font-bold text-slate-800">Control & Coord.</h3>
                        <p class="text-[10px] text-slate-500 mt-0.5">Nervous & Plant Hormones</p>
                    </div>

                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-100 text-center">
                        <div class="w-8 h-8 mx-auto mb-2 rounded-lg bg-indigo-500/10 text-indigo-600 flex items-center justify-center">
                            <i class="fa-solid fa-dna text-sm"></i>
                        </div>
                        <h3 class="text-xs font-bold text-slate-800">Heredity</h3>
                        <p class="text-[10px] text-slate-500 mt-0.5">Mendel Laws & Genetics</p>
                    </div>

                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-100 text-center">
                        <div class="w-8 h-8 mx-auto mb-2 rounded-lg bg-teal-500/10 text-teal-600 flex items-center justify-center">
                            <i class="fa-solid fa-leaf text-sm"></i>
                        </div>
                        <h3 class="text-xs font-bold text-slate-800">Our Environment</h3>
                        <p class="text-[10px] text-slate-500 mt-0.5">Ecosystems & Food Webs</p>
                    </div>
                </div>

                <!-- Start Action -->
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                    <button onclick="startQuiz()" class="w-full sm:w-auto px-8 py-4 bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-bold rounded-2xl shadow-lg shadow-emerald-500/25 transition-all transform hover:-translate-y-0.5 active:translate-y-0 flex items-center justify-center gap-2 text-base">
                        <span>Start Quiz Challenge</span>
                        <i class="fa-solid fa-arrow-right text-sm"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- 2. ACTIVE QUIZ SCREEN -->
        <div id="quiz-screen" class="hidden max-w-3xl w-full">
            <div class="glass-card rounded-3xl p-6 sm:p-8 shadow-2xl space-y-6">
                
                <!-- Progress Header -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-xs font-semibold text-slate-500">
                        <span id="question-tracker">Question 1 of 10</span>
                        <span id="category-badge" class="px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-200">Life Processes</span>
                    </div>
                    <div class="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden">
                        <div id="progress-bar" class="bg-gradient-to-r from-emerald-500 to-teal-500 h-full w-0 transition-all duration-300"></div>
                    </div>
                </div>

                <!-- Question Text -->
                <div class="min-h-[70px]">
                    <h3 id="question-text" class="text-lg sm:text-xl font-bold text-slate-900 leading-snug">
                        Loading question...
                    </h3>
                </div>

                <!-- Options Grid -->
                <div id="options-container" class="space-y-3">
                    <!-- Dynamic Answer Options inserted here -->
                </div>

                <!-- Detailed Explanation Card -->
                <div id="explanation-box" class="hidden p-4 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-2">
                    <div class="flex items-center gap-2 text-xs font-bold text-slate-700">
                        <i class="fa-solid fa-circle-info text-emerald-600"></i>
                        <span>Detailed Concept Explanation</span>
                    </div>
                    <p id="explanation-text" class="text-xs sm:text-sm text-slate-600 leading-relaxed"></p>
                </div>

                <!-- Navigation Controls -->
                <div class="flex justify-end pt-2 border-t border-slate-100">
                    <button id="next-btn" onclick="nextQuestion()" disabled class="px-6 py-3 bg-slate-200 text-slate-400 font-bold rounded-xl transition-all flex items-center gap-2 text-sm cursor-not-allowed">
                        <span>Next Question</span>
                        <i class="fa-solid fa-chevron-right text-xs"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- 3. FINAL RESULTS SCREEN -->
        <div id="result-screen" class="hidden max-w-2xl w-full text-center">
            <div class="glass-card rounded-3xl p-8 sm:p-10 shadow-2xl space-y-6">
                <div class="w-20 h-20 bg-emerald-100 text-emerald-600 rounded-3xl flex items-center justify-center mx-auto shadow-inner">
                    <i class="fa-solid fa-trophy text-3xl"></i>
                </div>

                <div>
                    <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900">Quiz Completed!</h2>
                    <p class="text-slate-500 text-sm mt-1">Here is a summary of your performance in Class 10 Biology</p>
                </div>

                <!-- Score Summary Cards -->
                <div class="grid grid-cols-3 gap-3 my-6">
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Total Score</span>
                        <p id="final-score" class="text-2xl sm:text-3xl font-extrabold text-emerald-600 mt-1">0/0</p>
                    </div>

                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Accuracy</span>
                        <p id="accuracy-percentage" class="text-2xl sm:text-3xl font-extrabold text-teal-600 mt-1">0%</p>
                    </div>

                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Time Taken</span>
                        <p id="total-time-taken" class="text-2xl sm:text-3xl font-extrabold text-indigo-600 mt-1">00:00</p>
                    </div>
                </div>

                <div class="pt-4 flex flex-col sm:flex-row gap-3 justify-center">
                    <button onclick="restartQuiz()" class="px-8 py-3.5 bg-gradient-to-r from-emerald-500 to-teal-600 text-white font-bold rounded-xl shadow-lg shadow-emerald-500/20 hover:from-emerald-600 hover:to-teal-700 transition-all flex items-center justify-center gap-2 text-sm">
                        <i class="fa-solid fa-rotate-right"></i>
                        <span>Try Quiz Again</span>
                    </button>
                </div>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="w-full bg-slate-900 border-t border-slate-800/80 py-4 text-center text-xs text-slate-500">
        <p>CBSE Class 10 Biology Interactive Practice Engine</p>
    </footer>

    <!-- Quiz Data & Logic -->
    <script>
        const quizQuestions = [
            {
                category: "Life Processes",
                question: "Which segment of the human alimentary canal primarily performs the absorption of water and salts from unabsorbed food material?",
                options: [
                    "Small intestine",
                    "Large intestine",
                    "Stomach",
                    "Esophagus"
                ],
                correct: 1,
                explanation: "While the small intestine is the main site for complete digestion and nutrient absorption, the large intestine specifically absorbs excess water and minerals from indigestible food waste."
            },
            {
                category: "Life Processes",
                question: "During anaerobic respiration in human muscle cells during strenuous physical exercise, pyruvate is converted into:",
                options: [
                    "Ethanol and Carbon dioxide",
                    "Lactic acid",
                    "Carbon dioxide and Water",
                    "Glucose"
                ],
                correct: 1,
                explanation: "When muscle cells experience lack of oxygen during heavy exercise, pyruvate is broken down via an anaerobic pathway to form Lactic Acid ($C_3H_6O_3$), which leads to muscle cramps."
            },
            {
                category: "Life Processes",
                question: "The correct sequence of anaerobic respiration occurring in yeast cells is:",
                options: [
                    "Glucose $\\rightarrow$ Pyruvate $\\rightarrow$ Ethanol + Carbon dioxide",
                    "Glucose $\\rightarrow$ Pyruvate $\\rightarrow$ Lactic Acid",
                    "Glucose $\\rightarrow$ Pyruvate $\\rightarrow$ Carbon dioxide + Water",
                    "Glucose $\\rightarrow$ Ethanol + Pyruvate"
                ],
                correct: 0,
                explanation: "In yeast, cytoplasm breaks glucose ($6$-carbon) into pyruvate ($3$-carbon), which in the absence of oxygen undergoes fermentation to yield ethanol, carbon dioxide, and energy."
            },
            {
                category: "Control & Coordination",
                question: "Which plant hormone promotes cell division and is present in high concentrations in seeds and fruits?",
                options: [
                    "Auxin",
                    "Gibberellin",
                    "Cytokinin",
                    "Abscisic Acid"
                ],
                correct: 2,
                explanation: "Cytokinins actively promote cell division. Therefore, they naturally occur in highest concentration in areas of rapid cell division like fruits and seeds."
            },
            {
                category: "Control & Coordination",
                question: "Which part of the human brain controls involuntary actions like blood pressure, salivation, and vomiting?",
                options: [
                    "Cerebrum",
                    "Cerebellum",
                    "Medulla in Hindbrain",
                    "Pons"
                ],
                correct: 2,
                explanation: "Involuntary actions such as blood pressure, salivation, and vomiting are regulated by the medulla located in the hindbrain."
            },
            {
                category: "Control & Coordination",
                question: "The gap between two neurons across which a chemical signal is transmitted is known as a:",
                options: [
                    "Dendrite",
                    "Axon",
                    "Synapse",
                    "Impulse"
                ],
                correct: 2,
                explanation: "A synapse is the microscopic gap between the axon terminal of one neuron and the dendrite of the next, where electrical signals convert into chemical neurotransmitters to cross over."
            },
            {
                category: "Heredity",
                question: "When a tall pea plant ($TT$) is crossed with a dwarf pea plant ($tt$), what proportion of plants in the $F_2$ generation will be tall?",
                options: [
                    "25%",
                    "50%",
                    "75%",
                    "100%"
                ],
                correct: 2,
                explanation: "In the $F_2$ generation of a monohybrid cross, the genotypic ratio is $1(TT) : 2(Tt) : 1(tt)$, giving a phenotypic ratio of $3$ Tall : $1$ Dwarf ($75\\%$ tall and $25\\%$ dwarf)."
            },
            {
                category: "Heredity",
                question: "What is the probability of a human male offspring inheriting an X chromosome from his father?",
                options: [
                    "0%",
                    "50%",
                    "75%",
                    "100%"
                ],
                correct: 0,
                explanation: "A male child receives a Y chromosome from his father and an X chromosome from his mother. Hence, the chance of inheriting an X chromosome from the father is $0\\%$."
            },
            {
                category: "Our Environment",
                question: "According to Lindeman's 10% law, if $10,000\\text{ J}$ of energy is available at the producer level, how much energy is available to the secondary consumer?",
                options: [
                    "$1000\\text{ J}$",
                    "$100\\text{ J}$",
                    "$10\\text{ J}$",
                    "$1\\text{ J}$"
                ],
                correct: 2,
                explanation: "Producers ($10,000\\text{ J}$) $\\rightarrow$ Primary Consumers ($1,000\\text{ J}$) $\\rightarrow$ Secondary Consumers ($100\\text{ J}$). Wait: $10\\%$ of $10,000 = 1000\\text{ J}$ (Primary), and $10\\%$ of $1000 = 100\\text{ J}$ (Secondary)."
            },
            {
                category: "Our Environment",
                question: "The synthetic chemicals responsible for the depletion of the protective Ozone layer in the upper atmosphere are:",
                options: [
                    "CFCs (Chlorofluorocarbons)",
                    "DDT (Dichlorodiphenyltrichloroethane)",
                    "Methane",
                    "Carbon Monoxide"
                ],
                correct: 0,
                explanation: "Chlorofluorocarbons (CFCs), widely used in refrigerants and fire extinguishers, release chlorine radicals in the stratosphere that break down ozone ($O_3$) molecules."
            }
        ];

        // Correct small math detail in Lindeman's question for strict accuracy:
        quizQuestions[8].options = ["$1000\\text{ J}$", "$100\\text{ J}$", "$10\\text{ J}$", "$1\\text{ J}$"];
        quizQuestions[8].correct = 1;

        // Quiz State Variables
        let currentQuestionIndex = 0;
        let score = 0;
        let userAnswers = [];
        let timerInterval = null;
        let secondsElapsed = 0;

        function startTimer() {
            secondsElapsed = 0;
            document.getElementById("header-timer").classList.remove("hidden");
            document.getElementById("header-timer").classList.add("flex");
            
            clearInterval(timerInterval);
            timerInterval = setInterval(() => {
                secondsElapsed++;
                const mins = String(Math.floor(secondsElapsed / 60)).padStart(2, '0');
                const secs = String(secondsElapsed % 60).padStart(2, '0');
                document.getElementById("timer-text").innerText = `${mins}:${secs}`;
            }, 1000);
        }

        function stopTimer() {
            clearInterval(timerInterval);
        }

        function startQuiz() {
            document.getElementById("welcome-screen").classList.add("hidden");
            document.getElementById("result-screen").classList.add("hidden");
            document.getElementById("quiz-screen").classList.remove("hidden");
            
            currentQuestionIndex = 0;
            score = 0;
            userAnswers = [];
            
            startTimer();
            renderQuestion();
        }

        function renderQuestion() {
            const q = quizQuestions[currentQuestionIndex];
            
            // Update Headers
            document.getElementById("question-tracker").innerText = `Question ${currentQuestionIndex + 1} of ${quizQuestions.length}`;
            document.getElementById("category-badge").innerText = q.category;
            document.getElementById("progress-bar").style.width = `${((currentQuestionIndex + 1) / quizQuestions.length) * 100}%`;
            
            // Question text
            document.getElementById("question-text").innerHTML = q.question;
            
            // Hide Explanation & Disable Next button
            document.getElementById("explanation-box").classList.add("hidden");
            const nextBtn = document.getElementById("next-btn");
            nextBtn.disabled = true;
            nextBtn.className = "px-6 py-3 bg-slate-200 text-slate-400 font-bold rounded-xl transition-all flex items-center gap-2 text-sm cursor-not-allowed";

            // Render Options
            const optionsContainer = document.getElementById("options-container");
            optionsContainer.innerHTML = "";

            const prefixLetters = ["A", "B", "C", "D"];

            q.options.forEach((optText, idx) => {
                const button = document.createElement("button");
                button.className = "option-btn w-full p-4 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-emerald-500 hover:bg-emerald-50/50 text-left font-medium text-slate-700 text-sm sm:text-base flex items-center justify-between group";
                button.onclick = () => selectOption(idx);

                button.innerHTML = `
                    <div class="flex items-center gap-3">
                        <span class="w-7 h-7 rounded-lg bg-slate-200/80 group-hover:bg-emerald-500 group-hover:text-white text-slate-600 font-bold text-xs flex items-center justify-center transition-colors">
                            ${prefixLetters[idx]}
                        </span>
                        <span class="option-label">${optText}</span>
                    </div>
                    <i class="status-icon fa-regular fa-circle text-slate-300"></i>
                `;
                optionsContainer.appendChild(button);
            });

            // Re-render MathJax formula markup if any
            if (window.MathJax) {
                MathJax.typesetPromise();
            }
        }

        function selectOption(selectedIndex) {
            const q = quizQuestions[currentQuestionIndex];
            const buttons = document.querySelectorAll(".option-btn");
            
            // Disable further selection on this question
            buttons.forEach(btn => btn.onclick = null);

            userAnswers.push(selectedIndex);

            if (selectedIndex === q.correct) {
                score++;
                buttons[selectedIndex].className = "option-btn w-full p-4 rounded-2xl bg-emerald-100 border-2 border-emerald-500 text-left font-semibold text-emerald-900 text-sm sm:text-base flex items-center justify-between";
                buttons[selectedIndex].querySelector(".status-icon").className = "status-icon fa-solid fa-circle-check text-emerald-600 text-lg";
            } else {
                buttons[selectedIndex].className = "option-btn w-full p-4 rounded-2xl bg-rose-100 border-2 border-rose-500 text-left font-semibold text-rose-900 text-sm sm:text-base flex items-center justify-between";
                buttons[selectedIndex].querySelector(".status-icon").className = "status-icon fa-solid fa-circle-xmark text-rose-600 text-lg";

                // Highlight correct option
                buttons[q.correct].className = "option-btn w-full p-4 rounded-2xl bg-emerald-50 border-2 border-emerald-400 text-left font-semibold text-emerald-800 text-sm sm:text-base flex items-center justify-between";
                buttons[q.correct].querySelector(".status-icon").className = "status-icon fa-solid fa-circle-check text-emerald-600 text-lg";
            }

            // Show explanation
            document.getElementById("explanation-text").innerHTML = q.explanation;
            document.getElementById("explanation-box").classList.remove("hidden");

            // Enable Next Button
            const nextBtn = document.getElementById("next-btn");
            nextBtn.disabled = false;
            nextBtn.className = "px-6 py-3 bg-gradient-to-r from-emerald-500 to-teal-600 text-white font-bold rounded-xl shadow-lg shadow-emerald-500/20 hover:from-emerald-600 hover:to-teal-700 transition-all flex items-center gap-2 text-sm cursor-pointer";

            if (window.MathJax) {
                MathJax.typesetPromise();
            }
        }

        function nextQuestion() {
            if (currentQuestionIndex < quizQuestions.length - 1) {
                currentQuestionIndex++;
                renderQuestion();
            } else {
                showResults();
            }
        }

        function showResults() {
            stopTimer();
            document.getElementById("quiz-screen").classList.add("hidden");
            document.getElementById("result-screen").classList.remove("hidden");

            document.getElementById("final-score").innerText = `${score}/${quizQuestions.length}`;
            const percentage = Math.round((score / quizQuestions.length) * 100);
            document.getElementById("accuracy-percentage").innerText = `${percentage}%`;

            const mins = String(Math.floor(secondsElapsed / 60)).padStart(2, '0');
            const secs = String(secondsElapsed % 60).padStart(2, '0');
            document.getElementById("total-time-taken").innerText = `${mins}:${secs}`;
        }

        function restartQuiz() {
            startQuiz();
        }
    </script>
</body>
</html>
```eof

### Summary of updates made:
1. **Complete Front Page Interface:** Built with a glassmorphism header, chapter overview cards, and a start button.
2. **Multi-Question Sequence:** Includes 10 board-exam-level questions covering **Life Processes**, **Control & Coordination**, **Heredity**, and **Our Environment**.
3. **Timer Component:** Built-in live header stopwatch that records total time taken.
4. **Detailed Explanations:** Explanations show instantly after answering each question.
5. **Final Result Dashboard:** Computes total score, percentage accuracy, and time taken at the end.
