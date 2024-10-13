from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

conn=sqlite3.connect('student.db')
cur=conn.cursor()
## Function To Load Google Gemini Model and provide queries as response

def  get_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the following schema - STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT,
    MARKS INTEGER);
    \nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    select all from the table - SELECT * FROM STUDENT;
    also dont include quoations like ``` for the query. And also dont give me any prompt just provide me with query
    """
]

## Streamlit App

st.set_page_config(page_title="Speech2Sql")
st.header("Speech2SQL - Transform voice into SQL")
st.header("Queries")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit or question:
   try:
      response= get_response(question,prompt)
      print(response)
      response=read_sql_query(response,"student.db")
      st.subheader("The Response is")
      if response:
        for row in response:
            print(row)
            st.header(row)
      else:
         st.header("Got Updated !")
         
   except:
      st.header("Wrong query !")