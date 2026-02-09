#!/usr/bin/env python3
"""
ATS-Friendly Resume Generator
Author: Emeka Anekwe
Description: Creates an ATS-optimized PDF resume using ReportLab
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors


def create_resume(output_filename="emeka_anekwe_resume_ats.pdf"):
    """
    Creates an ATS-friendly resume PDF.
    
    Args:
        output_filename (str): Name of the output PDF file
    """
    
    # Create PDF document with proper margins
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        rightMargin=1,
        leftMargin=1,
        topMargin=1,
        bottomMargin=1
    )

    # Get base styles
    styles = getSampleStyleSheet()

    # ==================== DEFINE CUSTOM STYLES ====================
    # You can modify colors, fonts, and sizes here
    
    # Header style (for your name)
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Heading1'],
        fontSize=25,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=6, # changed from 6
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    # Contact info style
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#333333'),
        alignment=TA_CENTER,
        spaceAfter=5
    )

    # Section header style (EDUCATION, WORK EXPERIENCE, etc.)
    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=3,
        spaceBefore=5,
        fontName='Helvetica-Bold',
        #borderPadding=4,
        #borderWidth=1,
        #borderColor=colors.HexColor('#1a1a1a'),
    )

    # Job title style
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=13,
        textColor=colors.HexColor('#1a1a1a'),
        fontName='Helvetica-Bold',
        spaceAfter=2
    )

    # Company/Institution style
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#444444'),
        fontName='Times-Italic',
        spaceAfter=4
    )

    # Bullet point style
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#333333'),
        leftIndent=20,
        spaceAfter=3,
        bulletIndent=10
    )

    # Body text style
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#333333'),
        spaceAfter=3
    )
    # Body text style
    small_message = ParagraphStyle(
        'SmallMessage',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#333333'),
        spaceAfter=1,
        leftIndent=420,
        fontName='Times-italic'
    )
    # ATS Message
    ats_message = ParagraphStyle(
        'ATSMessage',
        parent=styles['Normal'],
        fontSize=5,
        textColor=colors.HexColor("#ffffff"),
        spaceAfter=1,
        leftIndent=0
    )

    # ==================== BUILD RESUME CONTENT ====================
    story = []

    # -------------------- HEADER --------------------
    story.append(Paragraph("ATS keywords", ats_message))
    story.append(Paragraph("EMEKA ANEKWE", header_style))

    # Contact Information
    story.append(Paragraph("<b>Phone:</b> +61 429-864-790  |  <b>Email:</b> ea.anekwe@gmail.com  |  <b>LinkedIn:</b> linkedin.com/in/emeka-programmer<br></br><b>GitHub:</b> github.com/emekaanekwe", contact_style))
    #story.append(Paragraph("ea.anekwe@gmail.com", contact_style))
    #story.append(Paragraph("linkedin.com/in/emeka-programmer", contact_style))
    #story.append(Paragraph("github.com/emekaanekwe", contact_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.black, spaceBefore=12, spaceAfter=12))
    
    
    
    # -------------------- EDUCATION --------------------
    story.append(Paragraph("EDUCATION", section_header_style))

    # Master's in AI
    story.append(Paragraph("Master of Artificial Intelligence", job_title_style))
    story.append(Paragraph("Monash University, Clayton, Victoria, Australia", company_style))
    story.append(Paragraph("Expected Graduation Date: July 2026", body_style))
    story.append(Spacer(1, 0.1*inch))

    # Master's in Philosophy
    story.append(Paragraph("Master of Philosophy", job_title_style))
    story.append(Paragraph("Northern Illinois University, DeKalb, Illinois, USA", company_style))
    story.append(Paragraph("Focus: Philosophy of Biology, Social and Political Philosophy", body_style))
    story.append(Paragraph("August 2011 - July 2013", body_style))
    story.append(Spacer(1, 0.1*inch))

    # Bachelor's
    story.append(Paragraph("Bachelor of Arts in Spanish, Minor in Japanese", job_title_style))
    story.append(Paragraph("University of Illinois at Urbana-Champaign, Champaign-Urbana, Illinois, USA", company_style))
    story.append(Paragraph("January 2007 - July 2009", body_style))
    story.append(Spacer(1, 0.1*inch))

    # Study Abroad - Japan
    story.append(Paragraph("Study Abroad", job_title_style))
    story.append(Paragraph("Kanda International University, Chiba, Japan", company_style))
    story.append(Paragraph("Focus: History and Sociology", body_style))
    story.append(Paragraph("March 2008 - August 2008", body_style))
    story.append(Spacer(1, 0.1*inch))

    # Study Abroad - Spain
    story.append(Paragraph("Study Abroad", job_title_style))
    story.append(Paragraph("University of the Basque Country, Bilbao, Spain", company_style))
    story.append(Paragraph("Focus: Basque History", body_style))
    story.append(Paragraph("January 2006 - March 2006", body_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.black, spaceBefore=12, spaceAfter=12))
    # -------------------- PROJECTS --------------------
    story.append(Paragraph("PROJECTS", section_header_style))

    # Project 1
    story.append(Paragraph("Building an End-to-End Adaptive Evolution Experiment Designer", job_title_style))
    story.append(Paragraph("December 2025 - Present", company_style))
    story.append(Paragraph(
        "Designing pipeline for population structure analysis using GMM-based population "
        "inference with Deep RL to optimize experiment sequences for adaptive experimental "
        "design in evolutionary biology.",
        body_style
    ))
    story.append(Paragraph("Tech Stack: Pytorch, SciPy, Gymnasium, Tensorboard, Plotly, Streamlit, Kimi", body_style))
    story.append(Spacer(1, 0.1*inch))

    # Project 2
    story.append(Paragraph("Planning a Agentic Transcriber and Eval Workflow for Therapy Services", job_title_style))
    story.append(Paragraph("January 2025 - Present", company_style))
    story.append(Paragraph(
        "A transcription service that is psychology and therapy-specific with strict evals"
        "and built-in patient confidentiality measures.",
        body_style
    ))
    story.append(Paragraph("Tech Stack: Pytorch, SciPy, Gymnasium, Plotly, Streamlit, Kimi", body_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.black, spaceBefore=12, spaceAfter=12))
    # -------------------- WORK EXPERIENCE --------------------
    story.append(Paragraph("WORK EXPERIENCE", section_header_style))

    # Job 1: Pedestrian Operations Specialist
    story.append(Paragraph("Pedestrian Operations Specialist", job_title_style))
    story.append(Paragraph("Google and Tech Mahindra", company_style))
    story.append(Paragraph("March 2023 - November 2023 | Full-Time", body_style))
    story.append(Paragraph(
        "• Completed detailed reports at the beginning and end of every workday regarding "
        "gas mileage, route plans, coverage data, and expenses",
        bullet_style
    ))
    story.append(Paragraph(
        "• Employed Google's navigation software, a company-issued car and a credit card "
        "as per protocol",
        bullet_style
    ))
    story.append(Paragraph(
        "• Covered all sections of sidewalk and small path on and around the Las Vegas Strip "
        "within a 6x2 mile area (total coverage approximately 300km) using Google's latest "
        "Trekker image capturing technology",
        bullet_style
    ))
    story.append(Spacer(1, 30))

    # Job 2: Software Developer Trainee
    story.append(Paragraph("Software Developer Full-Stack Trainee", job_title_style))
    story.append(Paragraph("Software Development Mastery, Inc.", company_style))
    story.append(Paragraph("May 2019 - August 2019 | Part-Time", body_style))
    story.append(Paragraph(
        "• Built several Javascript and React applications from the ground up, including a digital clock, a rock-papers-scissors game, and a calculator",
        bullet_style
    ))
    story.append(Paragraph(
        "• Achieved the necessary working deadlines when collaborating with a team, and learning "
        "how to explain my work in a concise and digestible way",
        bullet_style
    ))
    story.append(Spacer(1, 0.1*inch))
    
    # Job 5: Lead Software Developer
    story.append(Paragraph("Lead Software Developer", job_title_style))
    story.append(Paragraph("University of Illinois Speech and Hearing Sciences Kirk Lab", company_style))
    story.append(Paragraph("August 2015 - August 2016 | Full-Time", body_style))
    story.append(Paragraph(
        "• Created, from scratch, a fully automated .exe using Matlab and Python that was designed "
        "to have authorized users listen to a randomized series of over 7,000 single-paired sounds "
        "with the goal of having the users discern which voice recording in a pair sounded more natural. "
        "After the session, the program would compile then organize the input data into a readable "
        "color-coded excel spreadsheet",
        bullet_style
    ))
    story.append(Paragraph(
        "• Engaged in scientific research on latest studies from articles on word recognition which "
        "were published by well-known professors, and presented my findings in our weekly meetings",
        bullet_style
    ))
    # Job 3: Tech Coach Manager
    story.append(Paragraph("Tech Coach Manager and Peer Advisor", job_title_style))
    story.append(Paragraph("Asurion LLC", company_style))
    story.append(Paragraph("December 2016 - June 2019 | Full-Time", body_style))
    story.append(Paragraph(
        "• Provided expert tech support to over 100 customers each shift ranging from factory "
        "resetting phones and accessing the ISP network, to re-registering IMEIs",
        bullet_style
    ))
    story.append(Paragraph(
        "• Maintained exceptional metrics that were consistent between the top 5%-25% out of "
        "over 9,000 Tech Experts throughout the enterprise",
        bullet_style
    ))
    story.append(Paragraph(
        "• Managed a team of 12 employees where I was tasked with listening to 70 calls per week, "
        "holding coaching sessions, and performing call data analysis into a self-made macro-based "
        "outlook template",
        bullet_style
    ))
    story.append(Spacer(1, 0.1*inch))

    # Job 4: Security Officer
    story.append(Paragraph("Security Officer and Dispatch Leader", job_title_style))
    story.append(Paragraph("MGM Resorts International", company_style))
    story.append(Paragraph("July 2016 - August 2019 | Full-Time", body_style))
    story.append(Paragraph(
        "• Issue out duties to other Officers when I am in the Security Dispatch Room. The duties "
        "range from helping a guest with wheelchair assistance, to fully organizing a life-or-death "
        "emergency situation that requires the Police, Fire Department, and Emergency Medical "
        "Response Teams to arrive",
        bullet_style
    ))
    story.append(Paragraph(
        "• Provide Top-level security service to property guests and conference participants using "
        "the fundamentals of S.H.O.W.",
        bullet_style
    ))
    story.append(Spacer(1, 0.1*inch))

    story.append(HRFlowable(width="100%", thickness=2, color=colors.black, spaceBefore=12, spaceAfter=12))
    # -------------------- TECHNICAL AND LANGUAGE SKILLS --------------------
    story.append(Paragraph("TECHNICAL AND LANGUAGE SKILLS", section_header_style))

    story.append(Paragraph("Coding:", job_title_style))
    story.append(Paragraph("Python, JavaScript, Java, R, Matlab, SQL, Bash Scripting, MiniZinc, PDDL 3.0", body_style))
    story.append(Spacer(1, 0.05*inch))
    
    story.append(Paragraph("AI Tools:", job_title_style))
    story.append(Paragraph("Cursor, LangGraph, LangSmith, Buzz Captions", body_style))
    story.append(Spacer(1, 0.05*inch))

    story.append(Paragraph("Operating Systems:", job_title_style))
    story.append(Paragraph("Windows, Mac, Linux (Ubuntu), NixOS, Raspberry Pi", body_style))
    story.append(Spacer(1, 0.05*inch))

    story.append(Paragraph("Software:", job_title_style))
    story.append(Paragraph(
        "VS Code, Cursor, IntelliJ, MS Office, Excel, PowerPoint, LibreOffice, PowerShell, CLI (Bash), Git, Bitbucket, "
        "Anaconda, Docker CLI, React.js, OBS Studio",
        body_style
    ))
    story.append(Spacer(1, 0.05*inch))

    story.append(Paragraph("Languages:", job_title_style))
    story.append(Paragraph("English, Spanish, Japanese", body_style))
    story.append(Paragraph("(Coded my resume using Python's ReportLab)", small_message))

    # ==================== BUILD THE PDF ====================
    doc.build(story)
    print(f"doc created: {output_filename}")


if __name__ == "__main__":
    # You can change the output filename here
    create_resume("ea_resume_8.pdf")