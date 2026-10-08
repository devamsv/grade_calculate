import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Title */
.main-title {
    text-align: center;
    color: white;
    font-size: 45px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #f3f4f6;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Form card */
.form-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.20);
    margin-bottom: 25px;
}

/* Section title */
.section-title {
    color: #4f46e5;
    font-size: 26px;
    font-weight: 700;
}

/* Metrics */
[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
    text-align: center;
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: #4f46e5;
    font-weight: 800;
}

/* Add button */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 25px;
    font-size: 16px;
    font-weight: 700;
    width: 100%;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: linear-gradient(90deg, #ee0979, #ff6a00);
    color: white;
}

/* Table */
[data-testid="stTable"] {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
}

/* Success message */
.stAlert {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Grade Function
# -----------------------------
def get_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">🎓 Student Grade Manager</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Manage student marks, grades and class performance</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Session State
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Add Student
# -----------------------------
st.markdown(
    '<div class="section-title">➕ Add New Student</div>',
    unsafe_allow_html=True
)

with st.form("add_student"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "👤 Student Name",
            placeholder="Enter student name"
        )

    with col2:
        mark = st.number_input(
            "📊 Mark",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    submitted = st.form_submit_button("🚀 Add Student")

    if submitted:

        if not name.strip():

            st.error("❌ Please enter a student name.")

        else:

            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(
                f"✅ {name} added successfully!"
            )


# -----------------------------
# Student Results
# -----------------------------
if st.session_state.students:

    st.markdown(
        '<div class="section-title">📋 Student Results</div>',
        unsafe_allow_html=True
    )

    st.table(st.session_state.students)

    # Get marks
    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    # Calculations
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    st.markdown(
        '<div class="section-title">📈 Class Performance</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📊 Class Average",
            f"{average:.1f}"
        )

    with col2:
        st.metric(
            "🏆 Highest Mark",
            highest
        )

    with col3:
        st.metric(
            "📉 Lowest Mark",
            lowest
        )

else:

    st.info(
        "🎯 No students added yet. Add your first student above!"
    )


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:white; font-size:15px;">
        🎓 Student Grade Manager | Week 1 · Day 4<br>
        Built with ❤️ using Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)