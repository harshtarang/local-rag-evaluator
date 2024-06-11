import pandas as pd
from datasets import Dataset 

def clean_answer_text(ans: str) -> str:
    return ans.replace("\n", "\\n")

answers = ["""
While I don't have real-time access to specific university requirements, I can provide you with general guidelines for Doctor of Audiology (Au.D.) program letter of recommendation requirements. It's always best to check the official university website for the most accurate and up-to-date information.

Generally, Au.D. programs require 3 letters of recommendation. These letters should come from:

    Academic advisors or professors who can speak to your academic abilities and potential for success in a graduate program.
    Clinical supervisors or professionals in the field of audiology who can attest to your practical skills, work ethic, and commitment to the profession.
    A third recommender who can provide additional insights into your character, motivation, or potential for success in a rigorous graduate program.

Letters should be written by individuals who know you well and can provide specific examples of your skills, accomplishments, and potential for success in an Au.D. program. It's essential to follow the application guidelines provided by the university, including any forms, deadlines, or submission instructions.
""",
"""
Graduate students at the University of Florida (UF) in the State University System can access the intellectual resources of faculty from other universities in several ways:

    Joint Degree Programs: UF offers joint degree programs with other universities in the State University System, allowing students to take courses and conduct research under the guidance of faculty from both institutions.
    Guest Lectures and Seminars: Many departments at UF invite faculty from other universities in the State University System to give guest lectures or seminars, providing students with the opportunity to learn from and interact with experts in their field.
    Research Collaborations: Graduate students can collaborate with faculty from other universities on research projects, either through formal collaborations or informal arrangements. This can provide students with access to additional resources and expertise.
    Inter-library Loan: UF's library system participates in inter-library loan programs, allowing students to borrow materials from other universities in the State University System.
    Online Resources: Many universities in the State University System make their resources available online, including academic articles, lectures, and other materials. Graduate students at UF can access these resources through their university's library website.
    Conferences and Workshops: Graduate students can attend conferences and workshops hosted by other universities in the State University System, providing opportunities to network with faculty and other students, and to learn about the latest research in their field.
    Consortium Programs: UF is a member of various consortium programs with other universities in the State University System, providing students with access to additional resources and opportunities for collaboration.

It is recommended that graduate students consult with their academic advisors or department chairs to learn more about the specific opportunities available to them.
""",
"""
The deadline for submitting freshman applications to the University of Florida for priority consideration in the admissions process is November 1st of the year preceding enrollment. It's important to note that applications received after this date will still be considered, but priority is given to those received by the deadline. For more information, you can visit the University of Florida's admissions website.
""",
"""
At the University of Florida (UF), there is no specific policy that restricts the number of terms a scholar can spend on their home campus during their graduate studies. However, UF encourages graduate students to take advantage of opportunities for study and research beyond their home campus, including other universities in the State University System.

To access resources from faculty at other universities in the State University System, students can consider the following options:

    Statewide Collaborative Programs: UF participates in several statewide collaborative programs, such as the Florida-Georgia Louis Stokes Alliance for Minority Participation (FL-LSAMP) and the Florida Water Resources Research Institute (FWRRI), which provide opportunities for students to work with faculty and researchers at other universities in the state.
    Inter-institutional Graduate Programs: UF offers inter-institutional graduate programs in partnership with other universities in the State University System, such as the Joint Graduate Program in Biomedical Engineering with the University of Central Florida.
    Visiting Scholar Programs: Many universities in the State University System have visiting scholar programs that allow graduate students to conduct research or take courses at their institutions for a limited period. Students should contact the graduate school or relevant department at the host university for more information.
    Consortium Agreements: UF has consortium agreements with several universities in the State University System, which allow students to take courses at the partner institution and receive credit towards their UF degree. Students should consult with their academic advisor or the UF Graduate School for more information.
    Online Resources: Many universities in the State University System offer online courses, lectures, and other resources that are accessible to students at other institutions. Students can check the websites of universities they are interested in to see what resources are available.

It is important to note that accessing resources from faculty at other universities may require additional steps, such as applying for admission or visiting scholar status, and may be subject to the policies and procedures of the host institution. Students should consult with their academic advisor or the UF Graduate School for more information.
""",
"""
At the University of Florida (UF), the unauthorized use of university keys or property is considered a serious offense and is strictly prohibited. This includes, but is not limited to:

    Unauthorized duplication or possession of university keys.
    Unauthorized use or access to university facilities, buildings, or property.
    Removing university property from designated areas without proper authorization.
    Tampering with or damaging university keys or property.
    Using university keys or property for personal gain or benefit.

Violations of these policies can result in disciplinary action, up to and including termination, expulsion, or legal action. It is important to always follow proper procedures and obtain necessary authorization before using university keys or property.
""",

"""
TEAMS (Teaching, Education, Administration and Management, and Student Services) and USPS (United States Postal Service) employees at the University of Florida (UF) are entitled to various forms of leave as outlined in the UF Employee Handbook (2019). Here are the details for each type of leave:

    Overtime Compensation: TEAMS employees are not eligible for overtime compensation as they are exempt from the Fair Labor Standards Act (FLSA). However, USPS employees are eligible for overtime compensation if they work more than 40 hours in a workweek. Overtime pay is calculated at a rate of one and one-half times the employee's regular rate of pay.
    Compensatory Time: TEAMS employees are not eligible for compensatory time. USPS employees may earn compensatory time at a rate of one and one-half hours for each hour of overtime worked, up to a maximum of 240 hours. USPS employees may choose to receive compensatory time off instead of overtime pay.
    Paid Holidays: UF observes 11 paid holidays per year for eligible employees. TEAMS and USPS employees are entitled to paid holidays if they are in a benefits-eligible position and have worked at least 1,040 hours in the 12 months preceding the holiday.
    Vacation Time: TEAMS employees earn vacation time based on their years of service, up to a maximum of 240 hours per year. USPS employees do not earn vacation time but are entitled to 13 days of annual leave per year, which increases with their length of service.
    Reporting Time: UF does not have a specific policy regarding reporting time for TEAMS or USPS employees. However, employees are expected to report to work as scheduled and may be subject to disciplinary action if they fail to do so.
    Sick Leave: TEAMS and USPS employees earn sick leave at a rate of eight hours per month, up to a maximum of 192 hours per year. Sick leave may be used for personal illness, injury, or medical appointments, as well as to care for a family member.
    Bereavement Leave: TEAMS and USPS employees are entitled to up to three days of paid bereavement leave in the event of the death of an immediate family member.
    Family and Medical Leave: Eligible TEAMS and USPS employees are entitled to up to 12 weeks of unpaid family and medical leave per year under the Family and Medical Leave Act (FMLA). FMLA leave may be used for the birth or adoption of a child, to care for a family member with a serious health condition, or for the employee's own serious health condition.
    Military Leave: TEAMS and USPS employees who are members of the National Guard or Reserves are entitled to up to 15 days of military leave per year. UF will continue to pay the employee's salary during military leave, up to a maximum of 30 days per fiscal year.
    Jury Duty Leave: TEAMS and USPS employees are entitled to unpaid leave to serve on a jury or to appear as a witness in a court proceeding. UF will continue to pay the employee's salary during jury duty leave, up to a maximum of $50 per day.

Note: The above information is based on the UF Employee Handbook (2019) and is subject to change. Employees should refer to the most recent version of the handbook or consult with their supervisor or HR representative for the most up-to-date information.
""",
"""
UF Staff regarding smoking cessation resources should familiarize themselves with the resources available to them through the UF Health Science Center’s Tobacco Free Program. This program offers a variety of resources to help employees quit smoking, including counseling, nicotine replacement therapy, and educational materials. Staff should also be aware of UF’s Smoke and Tobacco Free Campus Policy, which prohibits smoking and the use of tobacco products on all UF property.

For workplace hazard reporting, UF staff should utilize the university’s online reporting system, called the Hazard/Near Miss Reporting System. This system allows employees to report any potential hazards or unsafe conditions in the workplace. Staff should also be familiar with the procedures for reporting injuries and illnesses, as outlined in the Employee Handbook.

Regarding time-limited appointments, job abandonment, voluntary resignations or retirements, off-the-job conduct and acknowledging the Employee Handbook receipt, UF staff should:

    Be aware of the terms and conditions of their time-limited appointments, including the duration of the appointment and any expectations for renewal.
    Understand the university’s policies regarding job abandonment, which may include termination of employment.
    Be aware of the procedures for voluntary resignation or retirement, including any required notice periods and the impact on benefits.
    Understand that off-the-job conduct may be subject to disciplinary action if it adversely affects the employee’s job performance or the university’s reputation.
    Acknowledge receipt of the Employee Handbook and review it regularly to stay informed of university policies and procedures.

It is important to note that the above information is a general guideline and the specific policies and procedures may vary depending on the employment contract, collective bargaining agreement, and the specifics of the situation. It is always recommended to consult with the HR department or legal counsel for any specific questions or concerns.
""",

"""
Sure, I'd be happy to help you with that! Here are the key components of getting an M.P.H. degree at the University of Florida:

    Concentration Areas: The University of Florida's M.P.H. program offers several concentration areas, including Biostatistics, Epidemiology, Health Policy and Management, Social and Behavioral Sciences, and Environmental Health. Each concentration area has its own set of required courses and objectives.

    Transfer Credits: Students may be able to transfer up to 15 credits of graduate-level coursework from another institution, provided that the courses are relevant to the M.P.H. program and have been taken within the past seven years. The decision to transfer credits is made on a case-by-case basis by the program director.

    Supervisory Committees: Each student is required to form a supervisory committee, which consists of at least three graduate faculty members. The committee is responsible for advising the student on their coursework and master's thesis.

    Language Requirements: There are no specific language requirements for the M.P.H. program at the University of Florida. However, students who are non-native English speakers may be required to provide evidence of English proficiency.

    Examinations: There are no comprehensive exams required for the M.P.H. program at the University of Florida. However, students may be required to take and pass certain courses with a grade of B or higher.

    Time Limitations: Students must complete their M.P.H. degree within seven years of being admitted to the program.

    Leaves of Absence: Students who need to take a leave of absence from the program must submit a written request to the program director. Leaves of absence are granted for up to one year and do not count towards the seven-year time limit.

    Master's Thesis: All M.P.H. students are required to complete a master's thesis, which involves conducting original research on a topic related to public health. The thesis must be approved by the student's supervisory committee and defended in a public presentation.

I hope that helps! Let me know if you have any further questions.
""",
"""
To participate in cooperative degree programs at the University of Florida (UF), graduate students typically need to obtain approvals from both the academic department and the college or school offering the cooperative program. Here are the general steps involved:

    Identify the Cooperative Program: Graduate students should first identify the cooperative degree program they are interested in and ensure that they meet the eligibility requirements.

    Consult the Academic Advisor: The student should consult with their academic advisor to discuss their interest in the cooperative program and to understand how it fits into their academic plan.

    Obtain Departmental Approval: The student needs to obtain approval from their academic department. This usually involves submitting a formal request or application to the department. The department will review the student's academic record and suitability for the program.

    Obtain College Approval: After obtaining departmental approval, the student must seek approval from the college or school offering the cooperative program. This typically involves submitting the departmental approval to the college, along with any additional required materials.

    Complete Necessary Paperwork: Once both the department and college approvals are obtained, the student will need to complete any necessary paperwork to officially enroll in the cooperative program.

Please note that the exact process may vary depending on the specific cooperative program and the policies of the academic department and college. Therefore, it's always a good idea for students to consult with their academic advisor or the graduate school for the most accurate and up-to-date information.
"""

           
]
df = pd.read_csv("ground_truth_admissions.csv")

print(len(df))
print(len(answers))

question_df = df.loc[:, ['question']]

df = df.assign(answer='')

for idx, ans in enumerate(answers):
    df.at[idx, 'answer'] = clean_answer_text(ans)
    df.at[idx, 'contexts'] = ['No context']

print(df.head())

df.to_csv("ground_truth_admissions_answers_norag_mixtral7b.csv")