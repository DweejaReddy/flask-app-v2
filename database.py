from sqlalchemy import create_engine, text
import os
connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(connection_string,
                       connect_args={"ssl"      :{
    "ssl_ca": "/etc/ssl/cert.pem"
  }})


def load_job_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row)
  return jobs

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs")
#   result_dicts = []
#   for row in result.all():
#     result_dicts.append(row)
#     print(row ,"\n")


# result_all = result.all() 
# print (type(result_all))
# print (type(result_all[0]))
# print(result_all)
# # first_result = result_all[0]
# # first_result_dict = (result_all[0].__dict__)
# # print(type(first_result_dicṭ))
# # print(first_result_dict)