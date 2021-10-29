
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import func, not_, desc, and_, extract
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from sqlalchemy.schema import MetaData

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
    process = relationship("Process",lazy=True)

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
        return session.query(Candidate).filter(Candidate.username == username).one() 

    @classmethod
    def get_all_candidate(cls):
        return session.query(Candidate).all()


class Process(Base):
    __tablename__ = "process"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    recruiter_id = Column(Integer, ForeignKey('recruiter.id'))
    processStep = relationship("ProcessStep",lazy=True)

    def __repr__(self):
        return str("\n<Process>\nid:{0}\ndescription:{1}\nrecruiter_id:{2}\n"
                    .format(self.id, self.description, self.recruiter_id))

    @classmethod
    def insert(cls, description):
        new_process = Process()
        new_process.description = description
        session.add(new_process)
        session.commit()    
    
    @classmethod
    def get_all_process(cls):
        return session.query(Process).all()


class ProcessStep(Base):
    __tablename__ = "process_step"
    id = Column(Integer, primary_key=True)
    status = Column(String)
    priority = Column(Integer)
    process_id = Column(Integer, ForeignKey('process.id'))

    def __repr__(self):
        return str("\n<ProcessStep>\nid:{0}\nstatus:{1}\npriority:{2}\n"
                    .format(self.id, self.status, self.priority))

    @classmethod
    def insert(cls, status, priority):
        new_process_step = ProcessStep()
        new_process_step.status = status
        new_process_step.priority = priority
        session.add(new_process_step)
        session.commit()    
    
    @classmethod
    def get_all_process_step(cls):
        return session.query(ProcessStep).all()


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

    def __repr__(self):
         return str("\n<JobOpening>\nid:{0}\nname:{1}\ndescription:{2}\ndate_published:{3}\njob_start_date:{4}\nnum_vacancy:{5}\n"
                    .format(self.id, self.name, self.description, self.date_published, self.job_start_date, self.num_vacancy) + 
                    "job_category_id:{0}\njob_position_id:{1}\ndescription:{2}\ncompany_id:{3}\nprocess_id:{4}\n" 
                    .format(self.job_category_id, self.job_position_id, self.description, self.company_id, self.process_id))


        # return str("\n<JobOpening>\nid:{0}\nname:{1}\ndescription:{2}\ndate_published:{3}\njob_start_date:{4}\nnum_vacancy:{5}\n"
        #             .format(self.id, self.name, self.description, self.date_published, self.job_start_date, self.num_vacancy) + 
        #             "job_category_id:{0}\njob_position_id:{1}\n" 
        #             .format(self.job_category_id, self.job_position_id))

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

    @classmethod
    def test_join(cls):
        return session.query(JobOpening,JobCategory,JobPosition)\
                        .join(JobCategory)\
                        .join(JobPosition)\
                        .filter(JobOpening.job_category_id == JobCategory.id)\
                        .filter(JobOpening.job_position_id == JobPosition.id)\
                        .all()



class JobCategory(Base):
    __tablename__ = "job_category"
    id = Column(Integer, primary_key=True)
    code = Column(Integer, unique=True)
    name = Column(String)
    description = Column(String)
    job_opening = relationship("JobOpening",lazy=True)

    def __repr__(self):
        return str("\n<JobCategory>\nid:{0}\ncode:{1}\nname:{2}\ndescription:{3}\n"
                    .format(self.id, self.code, self.name, self.description))

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

    def __repr__(self):
        return str("\n<JobPosition>\nid:{0}\nname:{1}\ndescription:{2}\n"
                    .format(self.id, self.name, self.description))

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


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    job_opening = relationship("JobOpening",lazy=True)

    def __repr__(self):
        return str("\n<Company>\nid:{0}\nname:{1}\ndescription:{2}\n"
                    .format(self.id, self.name, self.description))

    @classmethod
    def insert(cls, name, description):
        new_company = Company()
        new_company.name = name
        new_company.description = description
        session.add(new_company)
        session.commit()    
    
    @classmethod
    def get_all_company(cls):
        return session.query(Company).all()



if __name__ == "__main__":
    # Base.metadata.create_all(engine)

    # ed_user = Recruiter()
    # Recruiter.insert('Smith', 'John', 'Doe', "123456", "123456")
    # Candidate.insert('u4', "u4@email.com", "123", "123", "u4", "test", "718000", "I am a QA Manager")
    # c = Candidate.get_all_candidate()
    # print(c)
    #now  = datetime.now()
    #JobOpening.insert("Software Architect", "work remotely 120k 5 days a week", now, now, 5, 2,2)
    # j = JobOpening.get_all_job_openings()
    # print(j)

    #JobCategory.insert(2, "Software Architect", "architect something")
    # c1 = JobCategory.get_all_job_category()
    # print(c1)
    #JobPosition.insert("Senior Software Architect", "design and develop entire software architecture")
    # now  = datetime.now()
    # JobOpening.insert("Software Engieer", "write something", now, now, 10, 1, 1)
    all = JobOpening.test_join()
    print(all)

    # def is_foreign_key(column):
    #     return True if column.foreign_keys else False
    # print(is_foreign_key(JobOpening.num_vacancy))

    # our_user = Recruiter.find_user("Smith")
    # print(our_user)