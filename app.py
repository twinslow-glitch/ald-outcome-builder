import streamlit as st

st.set_page_config(page_title="ALD Outcome Builder", page_icon="📝", layout="centered")

# Embedded banks so the app deploys cleanly on Streamlit Community Cloud
purpose_bank = {
  "To describe": {
    "functions": [
      "classifying",
      "describing attributes",
      "comparing",
      "generalising"
    ],
    "stems": [
      "X can be categorised into\u2026",
      "It is characterised by\u2026",
      "Compared with\u2026",
      "In general\u2026"
    ]
  },
  "To explain": {
    "functions": [
      "defining",
      "sequencing",
      "cause and effect",
      "clarifying"
    ],
    "stems": [
      "X is defined as\u2026",
      "First\u2026, then\u2026",
      "This happens because\u2026",
      "In other words\u2026"
    ]
  },
  "To justify": {
    "functions": [
      "giving reasons",
      "supporting with evidence",
      "qualifying claims"
    ],
    "stems": [
      "This is due to\u2026",
      "The evidence suggests\u2026",
      "This indicates that\u2026",
      "To a certain extent\u2026"
    ]
  },
  "To analyse": {
    "functions": [
      "identifying",
      "comparing",
      "inferring",
      "explaining relationships"
    ],
    "stems": [
      "This suggests\u2026",
      "In contrast\u2026",
      "A key factor is\u2026",
      "This is linked to\u2026"
    ]
  },
  "To evaluate": {
    "functions": [
      "judging",
      "weighing evidence",
      "drawing conclusions",
      "recommending"
    ],
    "stems": [
      "Overall\u2026",
      "The most significant\u2026",
      "On balance\u2026",
      "I would recommend\u2026"
    ]
  },
  "To argue / persuade": {
    "functions": [
      "stating a position",
      "persuading",
      "conceding",
      "counter-arguing"
    ],
    "stems": [
      "I would argue that\u2026",
      "It is clear that\u2026",
      "Although\u2026, \u2026",
      "However, \u2026"
    ]
  },
  "To instruct": {
    "functions": [
      "sequencing",
      "giving commands",
      "specifying conditions",
      "warning"
    ],
    "stems": [
      "First\u2026, then\u2026",
      "Ensure that\u2026",
      "If\u2026, then\u2026",
      "Do not\u2026"
    ]
  },
  "To recount": {
    "functions": [
      "sequencing events",
      "referencing time",
      "describing actions"
    ],
    "stems": [
      "At first\u2026",
      "Later\u2026",
      "Subsequently\u2026",
      "Finally\u2026"
    ]
  },
  "To reflect": {
    "functions": [
      "expressing viewpoint",
      "reviewing learning",
      "considering next steps"
    ],
    "stems": [
      "I realised that\u2026",
      "I found it challenging to\u2026",
      "Next time I will\u2026",
      "I have improved by\u2026"
    ]
  },
  "To synthesise information": {
    "functions": [
      "summarising",
      "selecting",
      "linking ideas",
      "integrating sources"
    ],
    "stems": [
      "The key points are\u2026",
      "Across the sources\u2026",
      "Taken together\u2026",
      "This aligns with\u2026"
    ]
  }
}
feature_groups = {
  "Connectors and logic": [
    "because",
    "therefore",
    "however",
    "although",
    "whereas",
    "consequently"
  ],
  "Evidence and reasoning frames": [
    "The evidence shows\u2026",
    "This suggests\u2026",
    "This indicates\u2026",
    "For example\u2026"
  ],
  "Comparative / evaluative language": [
    "more/less",
    "most significant",
    "on balance",
    "to a certain extent"
  ],
  "Subject vocabulary": [
    "Tier 2/3 words",
    "student-friendly definitions",
    "morphology (prefix/suffix)",
    "word families"
  ],
  "Noun phrases and nominalisation": [
    "expanded noun phrases",
    "nominalisation (evaporate \u2192 evaporation)",
    "dense academic phrasing"
  ],
  "Precision moves": [
    "hedging (may/might)",
    "modality (must/should)",
    "quantifiers (some/most)",
    "units/symbols"
  ],
  "Cohesion": [
    "this/these",
    "former/latter",
    "pronoun reference",
    "repetition for clarity"
  ],
  "Sentence structure": [
    "complex sentences",
    "passive voice (is caused by\u2026)",
    "conditionals (if\u2026 then\u2026)"
  ]
}
teach_fast_options = [
  "Model + annotate (3 min)",
  "Guided stems (5 min)",
  "Mid-lesson upgrade (2 min)",
  "Exit ticket rehearsal (3 min)"
]
evidence_options = [
  "One photo of student work",
  "Exit ticket",
  "Short paragraph / worked solution",
  "Oral explanation (teacher note)",
  "Annotation on a diagram / text"
]

st.title("ALD Outcome Builder")
st.caption("A quick form to generate a clear Academic Language Development outcome teachers can use immediately.")

with st.expander("How it works", expanded=False):
    st.write("Pick 1 purpose, 2–3 functions, and 1–2 language features. Add the content focus and a simple evidence check. Then generate a ready-to-copy outcome.")

col1, col2 = st.columns(2)
with col1:
    subject = st.text_input("Subject (optional)", placeholder="e.g., Science, Maths, English")
with col2:
    year_level = st.text_input("Year level (optional)", placeholder="e.g., Year 7")

purpose = st.selectbox("1) Lesson language purpose", options=list(purpose_bank.keys()) + ["Other"], index=1)

if purpose != "Other":
    function_options = purpose_bank[purpose]["functions"] + ["Other"]
else:
    function_options = ["Other"]

functions = st.multiselect(
    "2) Language functions (choose 2–3)",
    options=function_options,
    default=function_options[:2] if len(function_options) > 1 else []
)

other_function = ""
if "Other" in functions:
    other_function = st.text_input("Other function", placeholder="e.g., hypothesising, interpreting data")

flat_features = []
for grp_name in feature_groups:
    for feat in feature_groups[grp_name]:
        flat_features.append(grp_name + " — " + feat)
flat_features.append("Other")

features = st.multiselect(
    "3) Language features (choose 1–2)",
    options=flat_features,
    default=flat_features[:1]
)

other_feature = ""
if "Other" in features:
    other_feature = st.text_input("Other feature", placeholder="e.g., using past tense accurately")

content_focus = st.text_area(
    "4) Content focus / task", 
    placeholder="e.g., explain how natural selection leads to adaptation; justify which graph best represents the data",
    height=90
)

evidence = st.selectbox("5) Evidence (choose 1)", options=evidence_options, index=1)
teach_fast = st.selectbox("Quick teaching move (choose 1)", options=teach_fast_options, index=0)

st.divider()

btn = st.button("Generate outcome", type="primary")

if btn:
    if not content_focus.strip():
        st.error("Add a content focus / task so the outcome is specific.")
    else:
        fn_list = [f for f in functions if f != "Other"]
        if other_function.strip():
            fn_list.append(other_function.strip())
        feat_list = [f.split(" — ", 1)[1] if " — " in f else f for f in features if f != "Other"]
        if other_feature.strip():
            feat_list.append(other_feature.strip())

        # Build clean, teacher-friendly text
        purpose_txt = purpose if purpose != "Other" else "________"

        # Convert common function labels to verb phrases so the sentence reads naturally
        fn_map = {
            "classifying": "classify",
            "describing attributes": "describe attributes",
            "comparing": "compare",
            "generalising": "generalise",
            "defining": "define",
            "sequencing": "sequence",
            "cause and effect": "explain cause and effect",
            "clarifying": "clarify",
            "giving reasons": "give reasons",
            "supporting with evidence": "support claims with evidence",
            "qualifying claims": "qualify claims",
            "identifying": "identify",
            "inferring": "infer",
            "explaining relationships": "explain relationships",
            "judging": "judge",
            "weighing evidence": "weigh evidence",
            "drawing conclusions": "draw conclusions",
            "recommending": "make a recommendation",
            "stating a position": "state a position",
            "persuading": "persuade",
            "conceding": "concede",
            "counter-arguing": "counter-argue",
            "giving commands": "give commands",
            "specifying conditions": "specify conditions",
            "warning": "warn",
            "sequencing events": "sequence events",
            "referencing time": "reference time",
            "describing actions": "describe actions",
            "expressing viewpoint": "express a viewpoint",
            "reviewing learning": "review learning",
            "considering next steps": "identify next steps",
            "summarising": "summarise",
            "selecting": "select key information",
            "linking ideas": "link ideas",
            "integrating sources": "integrate sources"
        }

        # Functions
        fn_list = [f for f in functions if f != "Other"]
        if other_function.strip():
            fn_list.append(other_function.strip())
        fn_verbs = [fn_map.get(f, f) for f in fn_list]

        # Features (strip group prefix) and also filter out pure connector words accidentally chosen
        feat_list_raw = [f.split(" — ", 1)[1] if " — " in f else f for f in features if f != "Other"]
        if other_feature.strip():
            feat_list_raw.append(other_feature.strip())

        # If someone selected a connector word set by mistake, keep only feature-like items
        connector_words = set(["because", "therefore", "however", "although", "whereas", "consequently"])
        feat_list = [x for x in feat_list_raw if x.strip().lower() not in connector_words]

        # Nicely join functions
        if len(fn_verbs) == 0:
            fn_txt = "________"
        elif len(fn_verbs) == 1:
            fn_txt = fn_verbs[0]
        elif len(fn_verbs) == 2:
            fn_txt = fn_verbs[0] + " and " + fn_verbs[1]
        else:
            fn_txt = ", ".join(fn_verbs[:-1]) + ", and " + fn_verbs[-1]

        # Nicely join features
        if len(feat_list) == 0:
            feat_txt = "________"
        elif len(feat_list) == 1:
            feat_txt = feat_list[0]
        elif len(feat_list) == 2:
            feat_txt = feat_list[0] + " and " + feat_list[1]
        else:
            feat_txt = ", \".join(feat_list[:-1]) + ", and " + feat_list[-1]

        header_bits = []
        if subject.strip():
            header_bits.append(subject.strip())
        if year_level.strip():
            header_bits.append(year_level.strip())
        header_line = " | ".join(header_bits)

        # Avoid awkward "to to" and make purpose clause grammatical
        purpose_clause = purpose_txt.lower()
        if purpose_clause.startswith("to \ "):
            purpose_clause = purpose_clause[3:]

        # Final outcome sentence
        if feat_txt == "________":
            outcome = "Students will " + fn_txt + " in order to " + purpose_clause + " " + content_focus.strip() + ", shown by " + evidence.lower() + "."
        else:
            outcome = "Students will " + fn_txt + " using " + feat_txt + " in order to " + purpose_clause + " " + content_focus.strip() + ", shown by " + evidence.lower() + "."

        st.subheader("Your ALD outcome")
        st.subheader("Your ALD outcome")
        if header_line:
            st.caption(header_line)
        st.code(outcome)

        st.subheader("Optional: student-friendly stems")
        if purpose != "Other":
            stems = purpose_bank[purpose]["stems"]
            st.write("\n".join(["- " + s for s in stems[:4]]))
        else:
            st.write("Add stems that match your chosen functions.")

        st.subheader("Quick teaching move")
        st.write(teach_fast)

        st.subheader("Copy-ready block")
        copy_block = "ALD outcome\n" + outcome + "\n\nFunctions\n" + fn_txt + "\n\nFeatures\n" + feat_txt + "\n\nEvidence\n" + evidence + "\n\nTeach\n" + teach_fast
        st.text_area("", value=copy_block, height=220)
