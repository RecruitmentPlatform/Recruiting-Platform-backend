
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import func, not_, desc, and_, extract
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime

from types import ClassMethodDescriptorType

# from models.settings import Base, session, relationship
from settings import Base, session, engine
from datetime import datetime


class Recruiter(Base):
    __tablename__ = 'recruiter'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    password_hash = Column(String)
    session_id = Column(String)
    # acviity_id = relationship("Process", lazy=True)
    def __repr__(self):
        return str("\n<Recruiter>\nid:{0}\nusername:{1}\nfirstname:{2}\nlastname:{3}\npassword_hash:{4}\nsession_id:{5}"\
                    .format(self.id, self.username, self.firstname, self.lastname, self.password_hash, self.session_id))
    
    @classmethod
    def insert(cls, username, firstname, lastname, password_hash, session_id):
        new_rec = Recruiter()
        new_rec.username = username
        new_rec.firstname = firstname
        new_rec.lastname = lastname
        new_rec.password_hash = password_hash
        new_rec.session_id = session_id
        session.add(new_rec)
        session.commit()
    
    @classmethod
    def get_recruiter(cls, username):
        return session.query(Recruiter).filter(Recruiter.username==username).one() 
    
    @classmethod
    def get_all_recruiter(cls):
        return session.query(Recruiter).all() 
    

class Candidate(Base):
    __tablename__ = 'candidate'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    phone = Column(Integer)
    password_hash = Column(String)
    session_id = Column(String)
    description = Column(String)
    # acviity_id = relationship("Application", lazy=True)
    def __repr__(self):
        return str("\n<Candidate>\nid:{0}\nusername:{1}\nfirstname:{2}\nlastname:{3}\nemail:{4}\nphone:{5}\n"
                    .format(self.id, self.username, self.firstname, self.lastname, self.email, self.phone) + 
                    "password_hash:{0}\nsession_id:{1}\ndescription:{2}"
                    .format(self.password_hash, self.session_id, self.description))

    @classmethod
    def insert(cls, username, email, password_hash, session_id, 
                    firstname = None, lastname = None, phone = None, description = None):
        new_candidate = Candidate()
        new_candidate.username = username
        new_candidate.email = email
        new_candidate.password_hash = password_hash
        new_candidate.session_id = session_id
        new_candidate.firstname = firstname
        new_candidate.lastname = lastname
        new_candidate.phone = phone
        new_candidate.description = description
        session.add(new_candidate)
        session.commit()

    @classmethod
    def get_candidate(cls, username):
        return session.query(Candidate).filter(Candidate.username==username).one() 

    @classmethod
    def get_all_candidate(cls):
        return session.query(Candidate).all()
    

class JobOpening(Base):
    __tablename__ = 'job_opening'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date_published = Column(DateTime, default=datetime.date)
    job_start_date = Column(DateTime, default=datetime.date)
    num_vacancy = Column(Integer)
    job_category_id = Column(Integer, ForeignKey('job_category.id'))
    job_position_id = Column(Integer, ForeignKey('job_position.id'))
    # company_id = Column(Integer, ForeignKey('company.id'))
    # process_id = Column(Integer, ForeignKey('process.id'))

    # @classmethod
    # def insert(cls, name, description, date_published, job_start_date, num_vacancy, 
    #                 job_category_id, job_position_id, company_id, process_id):
    #     new_job = JobOpening()
    #     new_job.name = name
    #     new_job.description = description
    #     new_job.date_published = date_published
    #     new_job.job_start_date = job_start_date
    #     new_job.num_vacancy = num_vacancy
    #     new_job.job_category_id = job_category_id
    #     new_job.job_position_id = job_position_id
    #     new_job.company_id  = company_id
    #     new_job.process_id = process_id
    #     session.add(new_job)
    #     session.commit()

    @classmethod
    def insert(cls, name, description, date_published, job_start_date, num_vacancy, 
                    job_category_id, job_position_id):
        new_job = JobOpening()
        new_job.name = name
        new_job.description = description
        new_job.date_published = date_published
        new_job.job_start_date = job_start_date
        new_job.num_vacancy = num_vacancy
        new_job.job_category_id = job_category_id
        new_job.job_position_id = job_position_id
        session.add(new_job)
        session.commit()
    
    @classmethod
    def get_all_job_openings(cls):
        return session.query(JobOpening).all()

class JobCategory(Base):
    __tablename__ = "job_category"
    id = Column(Integer, primary_key=True)
    code = Column(Integer, unique=True)
    name = Column(String)
    description = Column(String)
    job_opening = relationship("JobOpening",lazy=True)

    @classmethod    
    def insert(cls, code, name, description):
        new_job_category = JobCategory()
        new_job_category.code = code
        new_job_category.name = name
        new_job_category.description = description
        session.add(new_job_category)
        session.commit()

    @classmethod
    def get_all_job_category(cls):
        return session.query(JobCategory).all()

    
class JobPosition(Base):
    __tablename__ = "job_position"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    job_opening = relationship("JobOpening",lazy=True)

    @classmethod
    def insert(cls, name, description):
        new_job_position = JobPosition()
        new_job_position.name = name
        new_job_position.description = description
        session.add(new_job_position)
        session.commit()    
    
    @classmethod
    def get_all_job_position(cls):
        return session.query(JobPosition).all()













if __name__ == "__main__":
    # Base.metadata.create_all(engine)

    # ed_user = Recruiter()
    # Recruiter.insert('Smith', 'John', 'Doe', "123456", "123456")
    # Candidate.insert('u4', "u4@email.com", "123", "123", "u4", "test", "718000", "I am a QA Manager")
    # c = Candidate.get_all_candidate()
    # print(c)

    # JobOpening.insert("Software Engineer", "work remotely 100k 5 days a week", datetime.date, datetime.date, 5, 1,1,1,1)
    # j = JobOpening.get_all_job_openings()
    # print(j)

    #JobCategory.insert(1, "Software Engineer", "write code")
    #c1 = JobCategory.get_all_job_category()
    #JobPosition.insert("Senior Software Enginner", "write code and review")
    # now  = datetime.now()
    # JobOpening.insert("Software Engieer", "write something", now, now, 10, 1, 1)
    all = JobOpening.get_all_job_openings()
    print(all)

    # our_user = Recruiter.find_user("Smith")
    # print(our_user)