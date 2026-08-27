import streamlit as st
import time

# Import auto-refresh component
try:
    from streamlit_autorefresh import st_autorefresh
    HAS_AUTOREFRESH = True
except ImportError:
    HAS_AUTOREFRESH = False

st.set_page_config(page_title="CBSE Class 10 Biology  Quiz ", layout="wide")
####i have kept it here

# Complete hide for menus, footers, badges, and the breakout fullscreen button
hide_streamlit_style = """
    <style>
    /* Hide top header & standard toolbar */
    #MainMenu {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    [data-testid="stHeader"] {visibility: hidden !important; display: none !important;}
    [data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
    
    /* Remove embed breakout fullscreen button */
    button[title="View fullscreen"] {display: none !important;}
    [data-testid="StyledFullScreenButton"] {display: none !important;}
    
    /* Hide bottom action buttons & viewer badges */
    [data-testid="stAppViewerOffer"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stStatusWidget"] {display: none !important;}
    div[class*="viewerBadge"] {display: none !important;}
    div[class*="styles_viewerBadge"] {display: none !important;}
    div[class*="stAppToolbar"] {display: none !important;}
    div[class*="stActionButton"] {display: none !important;}
    div[class*="manageApp"] {display: none !important;}
    #stDecoration {display: none !important;}
    </style>
"""
####i have kept it here

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "balloons_shown" not in st.session_state:
    st.session_state.balloons_shown = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# ==========================================
# SIDEBAR: TIMER & CONFIGURATION OPTIONS
# ==========================================

st.sidebar.header("⏱️ Quiz Mode & Timer")
timer_mode = st. sidebar.radio(
    "Choose Quiz Mode:",
    ["Without Timer (Practice Mode)", "With Timer (Exam Mode)"],
    disabled=st.session_state.quiz_started
)

time_limit_sec = 0
if timer_mode == "With Timer (Exam Mode)":
    time_limit_min = st.sidebar.number_input(
        "Set Time Limit (in minutes):",
        min_value=1,
        max_value=180,
        value=30,
        step=1,
        disabled=st.session_state.quiz_started
    )
    time_limit_sec = time_limit_min * 60

    # Auto-refresh every 1000ms (1 second) when quiz is running
    if HAS_AUTOREFRESH and st.session_state.quiz_started and not st.session_state.quiz_submitted:
        st_autorefresh(interval=1000, key="quiz_timer_refresh")

# Reset / Restart Quiz Button
if st.sidebar.button("🔄 Restart / Reset Quiz"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

sidebar_timer_placeholder = st.sidebar.empty()

# ==========================================
# MAIN HEADER & DUAL TIMER DISPLAY
# ==========================================

col_title, col_timer = st.columns([3, 1])

with col_title:
    st.title("CBSE Class 10 Biology Board Revision Quiz")

main_timer_placeholder = col_timer.empty()
warning_banner_placeholder = st.empty()

# Timer Logic & Execution
if timer_mode == "With Timer (Exam Mode)":
    if not st.session_state.quiz_started:
        sidebar_timer_placeholder.info("⏳ Waiting for you to start the test.")
        main_timer_placeholder.info("⏳ Press Start Test below")
    elif st.session_state.quiz_started and not st.session_state.quiz_submitted:
        elapsed_time = int(time.time() - st.session_state.start_time)
        remaining_time = time_limit_sec - elapsed_time

        if remaining_time > 0:
            mins, secs = divmod(remaining_time, 60)
            time_text = f"⏳ **Time Left:** {mins:02d}:{secs:02d}"

            if remaining_time <= 60:
                warning_banner_placeholder.error("⚠️ **LAST MINUTE WARNING:** Less than 1 minute remaining!")
                sidebar_timer_placeholder.error(time_text)
                main_timer_placeholder.error(time_text)
            else:
                sidebar_timer_placeholder.warning(time_text)
                main_timer_placeholder.warning(time_text)
        else:
            sidebar_timer_placeholder.error("🚨 **Time's Up!**")
            main_timer_placeholder.error("🚨 **Time's Up!**")
            st.session_state.quiz_submitted = True
            st.rerun()
else:
    sidebar_timer_placeholder.info("ℹ️ Practice Mode active.")
    main_timer_placeholder.info("ℹ️ No time limit")

# ==========================================
# QUESTION BANK ( 75 QUESTIONS)
# ==========================================


# ==============================================================================
# CLASS 10 BIOLOGY COMPLETE QUESTION BANK & INTERACTIVE QUIZ SYSTEM
# ==============================================================================

questions_db = [
    # --------------------------------------------------------------------------
    # CHAPTER: LIFE PROCESSES
    # --------------------------------------------------------------------------
    {
        "chapter": "Life Processes",
        "question": "Large intestine in man mainly carries out:",
        "options": [
            "(a) absorption of water",
            "(b) assimilation",
            "(c) digestion of fats",
            "(d) digestion of carbohydrates",
        ],
        "answer": "(a) absorption of water",
        "explanation": "The primary function of the large intestine is absorbing remaining water and salts from unabsorbed food material.",
    },
    {
        "chapter": "Life Processes",
        "question": "Select the correct statement regarding heterotrophs.",
        "options": [
            "(a) Heterotrophs make their own food.",
            "(b) Heterotrophs utilize solar energy to make food.",
            "(c) Heterotrophs do not make their own food.",
            "(d) Heterotrophs convert carbon dioxide and water into carbohydrates.",
        ],
        "answer": "(c) Heterotrophs do not make their own food.",
        "explanation": "Heterotrophs rely on organic matter produced by autotrophs because they lack photosynthetic pigments.",
    },
    {
        "chapter": "Life Processes",
        "question": "Which of the following chemical reactions occurs during photosynthesis?",
        "options": [
            "(a) Carbon dioxide is reduced and water is oxidised",
            "(b) Water is reduced and carbon dioxide is oxidised",
            "(c) Carbon dioxide and water are oxidised",
            "(d) Carbon dioxide and water are reduced",
        ],
        "answer": "(a) Carbon dioxide is reduced and water is oxidised",
        "explanation": "Light reactions split/oxidise water into oxygen, while dark reactions reduce carbon dioxide into carbohydrates.",
    },
    # --------------------------------------------------------------------------
    # CHAPTER: CONTROL AND COORDINATION
    # --------------------------------------------------------------------------
    {
        "chapter": "Control and Coordination",
        "question": "Consider the following statements:\n(a) Junction between two neurons is called synapse.\n(b) Ductless glands manufacture hormones and secrete them directly into the blood stream.\nWhich of these statement(s) is/are correct?",
        "options": [
            "(a) a only",
            "(b) b only",
            "(c) Both a and b",
            "(d) Neither a nor b",
        ],
        "answer": "(c) Both a and b",
        "explanation": "Synapses bridge neuronal gaps chemically, and endocrine (ductless) glands release hormones directly into circulation.",
    },
    {
        "chapter": "Control and Coordination",
        "question": "Co-ordination is achieved through nervous system as well as endocrine system by respective agents like:",
        "options": [
            "(a) neurotransmitters and proteins",
            "(b) neurotransmitters and hormones",
            "(c) neurotransmitters and sugars",
            "(d) sugars and hormones",
        ],
        "answer": "(b) neurotransmitters and hormones",
        "explanation": "Nervous systems transmit signals via electrical impulses/neurotransmitters; endocrine systems utilize chemical messengers called hormones.",
    },
    {
        "chapter": "Control and Coordination",
        "question": "There was a cerebellar dysfunction in a patient. Which of the following activities will get disturbed in this patient?",
        "options": [
            "(a) Salivation",
            "(b) Hunger control",
            "(c) Posture and balance",
            "(d) Regulation of blood pressure",
        ],
        "answer": "(c) Posture and balance",
        "explanation": "The cerebellum controls motor coordination, balance, and postural stability.",
    },
    {
        "chapter": "Control and Coordination",
        "question": "Identify the phytohormone:\n(I) It helps in growth of the stem.\n(II) It can cause formation of seedless fruits.",
        "options": [
            "(a) Cytokinin",
            "(b) Gibberellin",
            "(c) Ethylene",
            "(d) Auxin",
        ],
        "answer": "(b) Gibberellin",
        "explanation": "Gibberellins induce internodal stem elongation and promote parthenocarpy (fruit formation without seeds).",
    },
    # --------------------------------------------------------------------------
    # CHAPTER: HEREDITY AND EVOLUTION
    # --------------------------------------------------------------------------
    {
        "chapter": "Heredity",
        "question": "In human beings, the sex of the child depends on whether:",
        "options": [
            "(a) The paternal chromosome is X (for girls) or Y (for boys)",
            "(b) The paternal chromosome is Y (for girls) or X (for boys)",
            "(c) The maternal chromosome is X (for girls) or Y (for boys)",
            "(d) The maternal chromosome is Y (for girls) or X (for boys)",
        ],
        "answer": "(a) The paternal chromosome is X (for girls) or Y (for boys)",
        "explanation": "Mothers pass down an X chromosome; sex determination depends entirely on whether sperm carries an X or Y chromosome.",
    },
    {
        "chapter": "Heredity",
        "question": "Which of the following carry hereditary characters to the offspring in an organism?",
        "options": [
            "(a) Ribosome",
            "(b) Chromosome",
            "(c) Mitochondria",
            "(d) Lysosome",
        ],
        "answer": "(b) Chromosome",
        "explanation": "Chromosomes housed in the nucleus carry genes made of DNA that specify inherited traits.",
    },
    {
        "chapter": "Heredity",
        "question": "Which one of the following cannot be explained on the basis of Mendel's law of dominance?",
        "options": [
            "(a) Alleles do not show any blending and both characters recover as such in F2 generation",
            "(b) Factors occur in pairs",
            "(c) The discrete unit controlling a particular character is called factor",
            "(d) Out of one pair of factors one is dominant and the other recessive",
        ],
        "answer": "(a) Alleles do not show any blending and both characters recover as such in F2 generation",
        "explanation": "The non-blending recovery of both traits in the F2 generation is explained by the Law of Segregation, not Dominance.",
    },
    {
        "chapter": "Heredity",
        "question": "A pea plant with purple flowers is heterozygous (Pp). The P and p alleles are located:",
        "options": [
            "(a) next to each other on the same chromosome.",
            "(b) at the same location on homologous chromosomes.",
            "(c) on the X and Y chromosomes.",
            "(d) some distance apart on the same chromosome.",
        ],
        "answer": "(b) at the same location on homologous chromosomes.",
        "explanation": "Alleles for a single gene reside at matching loci on homologous chromosome pairs.",
    },
    {
        "chapter": "Heredity",
        "question": "The human body with XY pair of chromosomes is called:",
        "options": ["(a) male", "(b) hybrid", "(c) female", "(d) dihybrid"],
        "answer": "(a) male",
        "explanation": "Males carry heteromorphic XY sex chromosomes, whereas females carry XX.",
    },
    {
        "chapter": "Heredity",
        "question": "What is the genotypic ratio formed in the progeny of a cross between black furred (Bb) and white furred (bb) rabbits?",
        "options": [
            "(a) 2 : 1 : 1",
            "(b) 1 : 1 : 1",
            "(c) 1 : 2 : 1",
            "(d) 1 : 1",
        ],
        "answer": "(d) 1 : 1",
        "explanation": "A test cross (Bb x bb) yields 50% Bb and 50% bb, forming a 1:1 ratio.",
    },
    {
        "chapter": "Heredity",
        "question": "Which of the following may be used to obtain the F2 generation?",
        "options": [
            "(a) Allowing flowers on a parent plant to be self-pollinated",
            "(b) Allowing flowers on an F1 plant to be self-pollinated",
            "(c) Cross-pollinating an F1 plant with a parent plant",
            "(d) Cross-pollinating two parent plants",
        ],
        "answer": "(b) Allowing flowers on an F1 plant to be self-pollinated",
        "explanation": "Self-fertilizing (selfing) the F1 progeny produces the F2 generation.",
    },
    {
        "chapter": "Heredity",
        "question": "A homozygous dominant guinea pig with black fur (BB) is crossed with white fur (bb). The F1 is self-crossed. What percentage of F2 is expected to show white fur?",
        "options": ["(a) 25%", "(b) 50%", "(c) 75%", "(d) 100%"],
        "answer": "(a) 25%",
        "explanation": "F2 genotypic outcome is 1 BB : 2 Bb : 1 bb. Homozygous recessive (bb - white) is 1 out of 4 (25%).",
    },
    {
        "chapter": "Heredity",
        "question": "In cattle, having horns is recessive (h) and polled/no horns is dominant (H). When cattle with horns (hh) are crossed with cattle without horns, offspring horns equaled non-horned. Which is true?",
        "options": [
            "(a) Both parents are homozygous dominant.",
            "(b) One parent is homozygous dominant.",
            "(c) Both parents are heterozygous.",
            "(d) One parent is heterozygous.",
        ],
        "answer": "(d) One parent is heterozygous.",
        "explanation": "Crossing hh (horned) with Hh (heterozygous polled) yields 1 Hh : 1 hh (50% horned and 50% polled).",
    },
    {
        "chapter": "Heredity",
        "question": "The genotype for height is Tt. What conclusion may be drawn from this?",
        "options": [
            "(a) The allele for height has at least two different genes.",
            "(b) There are at least two different alleles for the gene for height.",
            "(c) There are two different genes for height, each having a single allele.",
            "(d) There is one allele for height with two different forms.",
        ],
        "answer": "(b) There are at least two different alleles for the gene for height.",
        "explanation": "Tt indicates two alternative forms (alleles T and t) for the height gene.",
    },
    {
        "chapter": "Heredity",
        "question": "Identify the correct sentence from the following:",
        "options": [
            "(a) Genotypic ratio of dihybrid cross is 9 : 3 : 3 : 1",
            "(b) Phenotype ratio of monohybrid cross is 1 : 2 : 1",
            "(c) Genotypic ratio of monohybrid cross is 1 : 2 : 1",
            "(d) Phenotypic ratio of dihybrid cross is 3 : 1",
        ],
        "answer": "(c) Genotypic ratio of monohybrid cross is 1 : 2 : 1",
        "explanation": "A monohybrid F2 cross yields 1 TT : 2 Tt : 1 tt genotypic ratio.",
    },
    {
        "chapter": "Heredity",
        "question": "'One of the allele is dominant over other'. This law is known as:",
        "options": [
            "(a) law of segregation",
            "(b) law of independent assortment",
            "(c) law of dominance",
            "(d) law of natural selection",
        ],
        "answer": "(c) law of dominance",
        "explanation": "Mendel's Law of Dominance states one allele masks the expression of another in heterozygous condition.",
    },
    {
        "chapter": "Heredity",
        "question": "A cross was carried out between two individuals heterozygous for two pairs of genes (AaBb x AaBb). The number of different genotypes and phenotypes obtained respectively are:",
        "options": [
            "(a) 4 and 9",
            "(b) 6 and 3",
            "(c) 9 and 4",
            "(d) 11 and 4",
        ],
        "answer": "(c) 9 and 4",
        "explanation": "A dihybrid cross produces 9 distinct genotypes and 4 distinct phenotypes (9:3:3:1 ratio).",
    },
    {
        "chapter": "Heredity",
        "question": "Which one of the following is NOT a direct conclusion drawn from Mendel's experiments?",
        "options": [
            "(a) Only one parental trait is expressed in F1",
            "(b) Two copies of each trait are inherited in sexually reproducing organisms",
            "(c) For recessive trait to be expressed, both copies should be identical",
            "(d) Natural selection can alter frequency of an inherited trait",
        ],
        "answer": "(d) Natural selection can alter frequency of an inherited trait",
        "explanation": "Natural selection concepts belong to Darwinian evolution rather than Mendel's transmission genetics laws.",
    },
    {
        "chapter": "Heredity",
        "question": "In sheep, dominant allele (B) produces black hair and recessive allele (b) produces white hair. When you see a black sheep, you would be able to identify:",
        "options": [
            "(a) its phenotype for hair colour.",
            "(b) its genotype for hair colour.",
            "(c) the genotypes for only one of its parents.",
            "(d) the genotypes for both of its parents.",
        ],
        "answer": "(a) its phenotype for hair colour.",
        "explanation": "Phenotype is observable appearance. A black sheep could carry either BB or Bb genotypes.",
    },
    {
        "chapter": "Heredity",
        "question": "Appearance of new combinations of characters in some progeny of F2 population indicates:",
        "options": [
            "(a) law of purity of gametes",
            "(b) law of independent assortment",
            "(c) law of dominance",
            "(d) none of the above",
        ],
        "answer": "(b) law of independent assortment",
        "explanation": "Recombinant traits occur because gene pairs assort independently into gametes.",
    },
    # --------------------------------------------------------------------------
    # CHAPTER: OUR ENVIRONMENT
    # --------------------------------------------------------------------------
    {
        "chapter": "Our Environment",
        "question": "The action of which among the following is crucial to the formation of ozone?",
        "options": [
            "(a) humans",
            "(b) sunlight",
            "(c) carbon dioxide",
            "(d) chlorofluorocarbons",
        ],
        "answer": "(b) sunlight",
        "explanation": "UV radiation from sunlight splits oxygen molecules into atomic oxygen to synthesize ozone (O3).",
    },
    {
        "chapter": "Our Environment",
        "question": "Disposable plastic plates should not be used because:",
        "options": [
            "(a) they are made of light weight materials",
            "(b) they are made of toxic materials",
            "(c) they are made of biodegradable materials",
            "(d) they are made of non-biodegradable materials",
        ],
        "answer": "(d) they are made of non-biodegradable materials",
        "explanation": "Plastics resist enzymatic digestion by decomposers, causing long-term waste issues.",
    },
    {
        "chapter": "Our Environment",
        "question": "Which of the following actions may NOT affect the environment in worse?",
        "options": [
            "(a) Plastic bags buried inside the earth",
            "(b) Planting of trees",
            "(c) Excessive use of non-biodegradable pesticides",
            "(d) Burning of plastic bags",
        ],
        "answer": "(b) Planting of trees",
        "explanation": "Aforestation improves ecological balance and air quality.",
    },
    {
        "chapter": "Our Environment",
        "question": "Which statement shows the interaction of an abiotic component with a biotic component?",
        "options": [
            "(a) A grasshopper feeding on a leaf",
            "(b) Rainwater running down into the lake",
            "(c) An earthworm making a burrow in the soil",
            "(d) A mouse fighting with another mouse for food",
        ],
        "answer": "(c) An earthworm making a burrow in the soil",
        "explanation": "An earthworm (biotic factor) interacts directly with soil (abiotic factor).",
    },
    {
        "chapter": "Our Environment",
        "question": "Which of the following belong to the same trophic level?",
        "options": [
            "(a) Cockroach and spider",
            "(b) Lizard and spider",
            "(c) Hawk and spider",
            "(d) Lizard and hawk",
        ],
        "answer": "(b) Lizard and spider",
        "explanation": "Both feed on primary consumers (insects), occupying the secondary consumer (3rd trophic) level.",
    },
    {
        "chapter": "Our Environment",
        "question": "What will happen if deer is missing in the food chain: Grass -> Deer -> Tiger?",
        "options": [
            "(a) The population of tiger increases.",
            "(b) The population of grass decreases.",
            "(c) Tiger will start eating grass.",
            "(d) The population of tiger decreases and the population of grass increases.",
        ],
        "answer": "(d) The population of tiger decreases and the population of grass increases.",
        "explanation": "Removing primary consumers deprives predators of food while allowing producers to grow unchecked.",
    },
    {
        "chapter": "Our Environment",
        "question": "Mandatory CFC-free refrigerators help prevent ozone depletion because:",
        "options": [
            "(a) This will help convert oxygen molecules into ozone.",
            "(b) This will help convert CFCs into ozone molecules.",
            "(c) This will reduce the production of CFCs from oxygen molecules.",
            "(d) This will reduce the release of CFCs that react with ozone molecules.",
        ],
        "answer": "(d) This will reduce the release of CFCs that react with ozone molecules.",
        "explanation": "Restricting CFC release prevents chlorine free-radical destruction of atmospheric stratospheric ozone.",
    },
    {
        "chapter": "Our Environment",
        "question": "First link in any food chain is usually green plants because:",
        "options": [
            "(a) Only green plants have the capacity to synthesize food using sunlight.",
            "(b) There are more herbivores than carnivores in a food chain.",
            "(c) Green plants are the only ones fixed at one place in the soil.",
            "(d) Green plants are widely distributed.",
        ],
        "answer": "(a) Only green plants have the capacity to synthesize food using sunlight.",
        "explanation": "Autotrophs capture solar energy to convert inorganic compounds into food.",
    },
    {
        "chapter": "Our Environment",
        "question": "Which of the following does NOT exist in a balanced ecosystem?",
        "options": [
            "(a) Interconnected food chains.",
            "(b) Interdependence among living organisms and the environment.",
            "(c) Animals dependent on plants but plants are not dependent on animals.",
            "(d) Communities made up of different populations of organisms.",
        ],
        "answer": "(c) Animals dependent on plants but plants are not dependent on animals.",
        "explanation": "Ecosystems feature mutual dependency (plants depend on animals for pollination, CO2, and nutrients).",
    },
    {
        "chapter": "Our Environment",
        "question": "Which of the following are environment-friendly practices?",
        "options": [
            "(a) Carrying cloth bags to put purchases in while shopping",
            "(b) Switching off unnecessary lights and fans",
            "(c) Walking to school instead of getting dropped on a motor vehicle ",
             "(d) All of the above",
        ],
        "answer": "(d) All of the above",
        "explanation": "All listed options reduce energy consumption, plastic waste, and carbon emissions.",
    },
    {
        "chapter": "Our Environment",
        "question": "Which of the following belongs exclusively to a group of biotic components?",
        "options": [
            "(a) Tree, water, soil, animals",
            "(b) Soil, animals, plants, sea",
            "(c) Animal, plants, microorganisms",
            "(d) Microorganisms, plants, soil, water",
        ],
        "answer": "(c) Animal, plants, microorganisms",
        "explanation": "Biotic factors consist purely of living organisms.",
    },
    {
        "chapter": "Our Environment",
        "question": "Which of the following pair is incorrectly matched?",
        "options": [
            "(a) Aquarium - An artificial ecosystem.",
            "(b) Parasite - Organism which lives in or on another organism.",
            "(c) Phytoplankton - Microscopic aquatic animals.",
            "(d) Ecology - Study of interactions among organisms and their environment.",
        ],
        "answer": "(c) Phytoplankton - Microscopic aquatic animals.",
        "explanation": "Phytoplankton are microscopic aquatic producers (plants/algae), whereas zooplankton are animals.",
    },
    # --------------------------------------------------------------------------
    # SECTION B: ASSERTION AND REASONING QUESTIONS (ALL CHAPTERS)
    # --------------------------------------------------------------------------
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Dominant allele is an allele whose phenotype expresses even in the presence of another allele.\nReason (R): A recessive allele produces its phenotype only when its paired allele on homologous chromosome is identical.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(b) Both A and R are true, but R is NOT the correct explanation of A.",
        "explanation": "Both definitions are genetically accurate, but defining a recessive allele does not explain the operational mechanism of dominance.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Traits like eye colour or height are inherited traits.\nReason (R): Inherited traits are not transferred from parents to young ones.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(c) A is true, but R is false.",
        "explanation": "Inherited traits are passed down genetically from parent to child across generations.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Chromosomes are known as hereditary units.\nReason (R): Chromosomes self-replicate and maintain properties through successive generations.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(a) Both A and R are true and R is the correct explanation of A.",
        "explanation": "Self-replication and stability of chromosomes enable accurate transfer of hereditary blueprints during cell division.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Mendel's principle of segregation is the principle of purity of gametes.\nReason (R): Gametes are pure for a character.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(a) Both A and R are true and R is the correct explanation of A.",
        "explanation": "Allelic separation ensures each gamete receives only one copy of an allele, maintaining gametic purity.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Inheritance provides both common basic design and subtle changes for the next generation.\nReason (R): Variations are maximised by sexual reproduction.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(b) Both A and R are true, but R is NOT the correct explanation of A.",
        "explanation": "Both statements are true facts of inheritance and sexual reproduction, but R does not directly account for basic design preservation.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Ozone is both beneficial and damaging.\nReason (R): Stratospheric ozone is formed by UV radiation acting on oxygen molecules.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(b) Both A and R are true, but R is NOT the correct explanation of A.",
        "explanation": "Ground ozone is toxic (damaging) while stratospheric ozone blocks radiation (beneficial). R describes stratospheric formation correctly but does not explain ground-level toxicity.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Garden is an artificial ecosystem.\nReason (R): Biotic and abiotic components of a garden are managed by humans.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(a) Both A and R are true and R is the correct explanation of A.",
        "explanation": "Human intervention in planting, soil care, and watering classifies gardens as artificial/man-made ecosystems.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Using jute bags is more environment-friendly than polythene bags.\nReason (R): Jute is biodegradable whereas polythene is non-biodegradable.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(a) Both A and R are true and R is the correct explanation of A.",
        "explanation": "Biodegradability allows natural decay by microbes, preventing long-term pollution.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Toxins accumulate more as we move up the food chain.\nReason (R): Substances not normally in biological tissue can magnify in concentration.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(a) Both A and R are true and R is the correct explanation of A.",
        "explanation": "Biomagnification happens because non-degradable chemicals cannot be excreted, increasing in concentration at successive trophic levels.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Biomagnification is caused by accumulation of biodegradable substances at each trophic level.\nReason (R): Biomagnification leads to maximum chemical accumulation in small fishes.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
            "(e) Both A and R are false.",
        ],
        "answer": "(e) Both A and R are false.",
        "explanation": "Biomagnification involves *non-biodegradable* substances, and top-level consumers (apex predators/humans) carry the maximum concentration, not small fish.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Green plants capture ~1% of sunlight falling on leaves into food energy.\nReason (R): An average of 10% of food eaten is turned into body biomass for the next consumer level.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(b) Both A and R are true, but R is NOT the correct explanation of A.",
        "explanation": "Both statements represent valid biological energy principles (1% solar absorption by autotrophs and 10% energy transfer rule), but R doesn't explain A.",
    },
    {
        "chapter": "Assertion & Reasoning",
        "question": "[ASSERTION-REASON]\nAssertion (A): Man is a herbivore.\nReason (R): Omnivores eat both plant food and animal meat.",
        "options": [
            "(a) Both A and R are true and R is the correct explanation of A.",
            "(b) Both A and R are true, but R is NOT the correct explanation of A.",
            "(c) A is true, but R is false.",
            "(d) A is false, but R is true.",
        ],
        "answer": "(d) A is false, but R is true.",
        "explanation": "Humans are omnivores, making the assertion false. The reason correctly defines omnivores.",
    },
]


# ==============================================================================
# QUIZ ENGINE EXECUTION MODULE
# ==============================================================================
def run_quiz(database):
    score = 0
    total = len(database)

    print("\n" + "=" * 60)
    print(f"       CLASS 10 BIOLOGY COMPREHENSIVE QUIZ ({total} QUESTIONS)")
    print("=" * 60 + "\n")

    for index, q in enumerate(database, start=1):
        print(f"[{q['chapter'].upper()}] Question {index} of {total}:")
        print(q["question"])
        print("-" * 40)
        for opt in q["options"]:
            print(f"  {opt}")

        user_choice = (
            input("\nYour Answer (a/b/c/d/e): ").strip().lower()
        )

        # Basic check matching option prefix letter
        correct_letter = q["answer"][1].lower()

        if user_choice == correct_letter:
            print("\n Correct!")
            score += 1
        else:
            print(f"\n Incorrect. Correct Answer: {q['answer']}")

        print(f"Explanation: {q['explanation']}\n")
        print("=" * 60 + "\n")

    print(f"QUIZ COMPLETED! Final Score: {score}/{total} ({(score/total)*100:.1f}%)")


if __name__ == "__main__":
    # Execute quiz runner
    run_quiz(questions_db)

