import numpy as np
import pandas as pd
import env

def acquire_logs():
    """
    This function will acquire the curriculum log data from the codeup database.
    It will use your env file for the necessary login info.
    """

    #Set the query
    logs_query = """
            SELECT date, time, path, user_id, name AS 'cohort', ip, start_date, end_date, program_id
            FROM logs LEFT JOIN cohorts ON cohorts.id = logs.cohort_id;
            """

    #Set the url
    logs_url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/curriculum_logs'

    #Get the data
    logs = pd.read_sql(logs_query, logs_url)

    return logs

def wrangle_logs():
    """
    This function will acquire and prepare the curriculum log data and return the prepared dataframe.
    """

    #Acquire the data
    logs = acquire_logs()

    #Begin preparing

    #Create new dataframe for program_id
    program = pd.DataFrame({
        'id':[1,2,3,4],
        'program':['PHP Full Stack Web Development',
                'Java Full Stack Web Development',
                'Data Science',
                'Front End Web Development'],
        'subdomain': ['php', 'java', 'ds', 'fe']
    })

    #Join new dataframe with logs dataframe
    logs = logs.merge(program, how = 'left', left_on = 'program_id', right_on = 'id').drop(columns = ['id', 'program_id'])

    #Convert date to datetime object and create new month, year, and day columns
    logs.date = pd.to_datetime(logs.date)
    logs['year'] = logs.date.dt.year
    logs['month'] = logs.date.dt.month_name()
    logs['day'] = logs.date.dt.day_name()

    #Convert the time column to a datetime object and create a new column for hour
    logs.time = pd.to_datetime(logs.time)
    logs['hour'] = logs.time.dt.hour

    # I don't think the time column will be useful now, so go ahead and drop it
    logs = logs.drop(columns = ['time'])

    #Create a column to determine whether or not the user is a graduate
    logs['is_graduate'] = (logs.date > logs.end_date) & (logs.cohort != 'Staff')

    #Create a column to determine whether or not the user is a current student
    logs['current_student'] = (logs.date <= logs.end_date) & (logs.cohort != 'Staff')

    #Create a column for each piece of the requested path and drop the original path column
    request_path_and_params = logs.path.str.split('/', expand=True)
    request_path_and_params.columns = ['request_section', 'request_subject', 'request_lesson', 'param_4', 'param_5', 'param_6', 'param_7', 'param_8']
    logs = logs.join(request_path_and_params)

    #Now convert 'date' to the index
    logs = logs.set_index('date').sort_index()

    return logs
