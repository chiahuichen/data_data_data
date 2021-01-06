import random
import pandas as pd

class ny_mega_millions:
    def __init__(self):
        """extract, clean, format data from a csv file from
         https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD
         """  
        # load csv file into dataframe 
        self.df = pd.read_csv('lottery.csv')[['Draw Date', 'Winning Numbers', 'Mega Ball']]
        # update column names
        self.df.columns = ['draw_date', 'whites', 'mega']
        # rearrange the date format from 'mm/dd/yyyy' to 'yyyy/mm/dd'
        for x in range(len(self.df)):
            self.revised = self.df['draw_date'][x][6:] + '/' + self.df['draw_date'][x][:5]
            self.df.at[x, 'draw_date'] = self.revised 
        # filter the rows. keep rows with draw_date range from 2008/01/01 to 2021/01/01
        # order the rows by draw_date
        self.df = self.df.loc[self.df['draw_date'].str.startswith(('2018', '2019', '2020', '2021'))].sort_values('draw_date')
        # reset row index(created a new column on the far left)
        self.df.reset_index(inplace=True)
        # drop the 'index' column (old index)
        self.df.drop(columns='index', inplace=True)
        # in each row, extract column 'whites' value(string), split it into a list, add value from df['mega']
        # then append the concatenated list to data
        self.data = []
        for x in range(len(self.df)):
            self.sub = [int(y) for y in self.df['whites'][x].split()]  + [int(self.df['mega'][x])]
            self.data.append(self.sub)
        # create a dataframe with data
        self.draws = pd.DataFrame(self.data, columns=['w1', 'w2', 'w3', 'w4', 'w5', 'mega'])
        # concate all white balls columns into a single series
        self._series = pd.concat((self.draws[x] for x in self.draws.columns[0:-1]))
        # 10 least_shown white balls (fact: all 70 balls drawn at least once)
        self.least_white = list(self._series.value_counts().tail(10).keys())
        # 3 least_shown mega ball
        self.least_mega = list(self.draws['mega'].value_counts().tail(3).keys())
        

    def top_millions(self, number=5):
        """return top 5 draws (default) with limit of 25, each draw with 5 white balls and a mega ball"""
        if number > 25:
            return "The limit is 25."
        top_lst = []  
        for x in self.draws.columns:  
            top_lst.append(self.draws[x].value_counts().head(number).keys())
        return list([x[y] for x in top_lst] for y in range(number))


    def random_millions(self, number=5):
        """random choose 5 white balls and a mega ball"""
        white = random.sample(list(range(1, 71)), 70)
        mega = random.sample(list(range(1, 26)), 25)
        random_list = []
        for x in range(number):
            random_list.append(random.sample(white, 5) + random.sample(mega, 1))
        return random_list

            
    def least_millions(self, number=5):
        """random draw from self.least_white and self.least_mega"""
        least_lst = []
        for x in range(number):
            least_lst.append(random.sample(self.least_white, 5) + random.sample(self.least_mega, 1))
        return least_lst
        
    

if __name__== '__main__':
    ny = ny_mega_millions()
    print('hot_numbers_combo', ny.top_millions())
    print('random_numbers_combo', ny.random_millions())
    print('cold_numbers_combo', ny.least_millions())
    
    







    
    
    




    
    
