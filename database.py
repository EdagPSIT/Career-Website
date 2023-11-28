from sqlalchemy import create_engine, text
import os

# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

# db_connection_string = os.environ['DB_CONNECTION_STRING']

db_connection_string = "mysql+pymysql://root:EdagPSIT#2024@localhost/joviancareers?charset=utf8mb4"
engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        columns = result.keys()  # Get column names
        for row in result.fetchall():
            job_dict = {}
            for idx, column in enumerate(columns):
                job_dict[column] = row[idx]
            jobs.append(job_dict)
        return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    row = result.fetchone()
    if row is None:
        return None
    else:
        columns = result.keys()
        job_dict = {column: value for column, value in zip(columns, row)}
        return job_dict


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    # query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    # conn.execute(query, 
    #              job_id=job_id, 
    #              full_name=data['full_name'],
    #              email=data['email'],
    #              linkedin_url=data['linkedin_url'],
    #              education=data['education'],
    #              work_experience=data['work_experience'],
    #              resume_url=data['resume_url'])
    query = text("""
        INSERT INTO applications 
        (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) 
        VALUES 
        (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
    """)
    
    params = {
        'job_id': job_id,
        'full_name': data['full_name'],
        'email': data['email'],
        'linkedin_url': data['linkedin_url'],
        'education': data['education'],
        'work_experience': data['work_experience'],
        'resume_url': data['resume_url']
    }

    conn.execute(query, params)
    conn.commit()
