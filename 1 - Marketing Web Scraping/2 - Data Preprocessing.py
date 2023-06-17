#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class preprocessing:
    def __init__(self, downloads_path, output_path, month_begin, month_end):
        self.downloads_path = downloads_path
        self.output_path = output_path
        self.month_begin =  self.month_begin
        self.month_end = self.month_end
        
    #=================== OVERVIEW ===================
    def overview(self):
        temp = []
        pd_path = self.downloads_path+'Overview'
        csv_files = glob.glob(os.path.join(path, "*.csv"))

        for f in csv_files:
            i = f.split("\\")[-1]
            #print(cut)
            df = pd.read_csv(pd_path+i, sep = ';')
            df.columns = df.columns.str.lower()
            temp.append(df)

        overview = pd.concat(temp, axis = 0, ignore_index = True)

        #Save as Excel
        overview_path = self.output_path+'overview.xlsx'
        writer = pd.ExcelWriter(overview_path,engine='xlsxwriter')
        data = overview.to_excel(writer, sheet_name = 'Лист 1', index = False)
        writer.save()

    #=================== BACKLINKS ANCHORS ===================
    def backlinks_anchors(self):
        temp = []

        for i in backlinks_anchors_list:
            filename = self.downloads_path+i+'-backlinks_anchors.csv'
            df = pd.read_csv(filename, sep = ";")
            #df.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
            df['Domain'] = i
            df.columns = df.columns.str.lower()
            temp.append(df)

        backlinks_anchors = pd.concat(temp, axis = 0, ignore_index = True)
        backlinks_anchors = pd.merge(backlinks_anchors, domains,on="domain",how="left")

        #Save as Excel
        backlinks_anchors_path = self.output_path+'backlinks_anchors.xlsx'
        writer = pd.ExcelWriter(backlinks_anchors_path,engine='xlsxwriter')
        data = backlinks_anchors.to_excel(writer, sheet_name = 'Лист 1', index = False)
        writer.save()

    #=================== BACKLINKS REFDOMAINS ===================    
    def backlinks_refdomains(self):
        temp = []

        for i in backlinks_refdomains_list:
            filename = self.downloads_path+i+'-backlinks_refdomains.csv'
            df = pd.read_csv(filename, sep = ";")
            #df.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
            df['Domain'] = i
            df.columns = df.columns.str.lower()
            temp.append(df)

        backlinks_refdomains = pd.concat(temp, axis = 0, ignore_index = True)
        backlinks_refdomains.fillna(0, inplace = True)

        backlinks_refdomains = pd.merge(backlinks_refdomains, domains,on="domain",how="left")

        #Save as Excel
        backlinks_refdomains_path = self.output_path+'backlinks_refdomains.xlsx'
        writer = pd.ExcelWriter(backlinks_refdomains_path,engine='xlsxwriter')
        data = backlinks_refdomains.to_excel(writer, sheet_name = 'Лист 1', index = False)
        writer.save()
        
    #=================== TREND BY DEVICES ===================
    def trend_by_devices(self):
        visits_temp = []
        unique_temp = []
        duration_temp = []
        bounce_temp = []
        
        trend_by_category_list = [visits_temp, unique_temp, duration_temp, bounce_temp]
        trend_by_name_list = ['visits', 'users', 'time_on_site', 'bounce_rate']
        
        self_list = [self.visits_list, self.unique_list, self.duration_list, self.bounce_rate_list]
        
        #first_month = (datetime.date.today() - relativedelta(months=6)).strftime('%b')
        #last_month = datetime.date.today().strftime('%b')
        
        first_month = self.month_begin # 'Mar'
        last_month = self.month_end # 'Sep'
        
        year = datetime.date.today().strftime('%Y')
        
        for index, list_ in enumerate(self_list):
            for domain in list_:
                filename = self.downloads_path+'Trend By Devices (domain='+i+', metric='+trend_by_name_list[index]+', \
                            range='+first_month+' – '+last_month+' '+year+', devices=all_devices,desktop,mobile).csv'
                df_temp = pd.read_csv(filename, sep = ",")
                df_temp.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
                df_temp['Domain'] = i
                df_temp.columns = df_temp.columns.str.lower()
                trend_by_category_list[index].append(df_temp)
            
        visits = pd.concat(visits_temp, axis = 0, ignore_index = True)
        visits.fillna(0, inplace = True)
        visits.rename(columns = {'all devices':'visits_devices', 'desktop':'visits_desktop','mobile':'visits_mobile'},
                      inplace = True)

        unique = pd.concat(unique_temp, axis = 0, ignore_index = True)
        unique.fillna(0, inplace = True)
        unique.rename(columns = {'all devices':'unique_devices', 'desktop':'unique_desktop','mobile':'unique_mobile'}, 
                      inplace = True)

        duration = pd.concat(duration_temp, axis = 0, ignore_index = True)
        duration.fillna(0, inplace = True)
        duration.rename(columns = {'all devices':'duration_devices', 'desktop':'duration_desktop','mobile':'duration_mobile'},
                        inplace = True)

        bounce = pd.concat(bounce_temp, axis = 0, ignore_index = True)
        bounce.fillna(0, inplace = True)
        bounce.rename(columns = {'all devices':'bounce_devices', 'desktop':'bounce_desktop','mobile':'bounce_mobile'},
                      inplace = True)

        trend_by_devices = pd.merge(visits, bounce, how='left', on = ['month', 'domain'])
        trend_by_devices = pd.merge(trend_by_devices, unique, how='left', on = ['month', 'domain'])
        trend_by_devices = pd.merge(trend_by_devices, duration, how='left', on = ['month', 'domain'])

        # bounce_all
        trend_by_devices['all_no_bounce'] = round((trend_by_devices['visits_devices'] \
                                                   * trend_by_devices['bounce_devices']).astype(float))
        trend_by_devices['all_bounce'] = round((trend_by_devices['visits_devices'] \
                                                - (trend_by_devices['visits_devices'] \
                                                   * trend_by_devices['bounce_devices'])).astype(float))

        # bounce_desktop
        trend_by_devices['desktop_no_bounce'] = round((trend_by_devices['visits_desktop'] \
                                                       * trend_by_devices['bounce_desktop']).astype(float))
        trend_by_devices['desktop_bounce'] = round((trend_by_devices['visits_desktop'] \
                                                    - (trend_by_devices['visits_desktop'] \
                                                       * trend_by_devices['bounce_desktop'])).astype(float))

        # bounce_mobile
        trend_by_devices['mobile_no_bounce'] = round((trend_by_devices['visits_mobile'] \
                                                      * trend_by_devices['bounce_mobile']).astype(float))
        trend_by_devices['mobile_bounce'] = round((trend_by_devices['visits_mobile'] \
                                                   - (trend_by_devices['visits_mobile'] * trend_by_devices['bounce_mobile'])).astype(float))

        trend_by_devices = pd.merge(trend_by_devices, domains,on="domain",how="left")

        #Month = Mon + Year
        trend_by_devices['year'] = (pd.DatetimeIndex(trend_by_devices['month']).year).astype("string")

        trend_by_devices['month'] = trend_by_devices['month_number'] = pd.DatetimeIndex(trend_by_devices['month']).month
        trend_by_devices['month_number'] = trend_by_devices['month_number'].astype("string")
        trend_by_devices['month'] = trend_by_devices['month_number'].apply(
                                    lambda x: (datetime.datetime.strptime(x, "%m")).strftime("%b"))

        #trend_by_devices['month'] = trend_by_devices['month'].apply(lambda x: calendar.month_abbr[x])
        #trend_by_devices['month_number'] = trend_by_devices['month'].apply(lambda x: datetime.datetime.strptime(x, "%b").month)

        trend_by_devices['month_year'] = (pd.to_datetime(trend_by_devices['month_number'] \
                                                         + ' ' + trend_by_devices['year'])).dt.strftime('%d.%m.%Y')

        #trend_by_devices['month_year'] = pd.to_datetime(trend_by_devices['month_year'])
        #trend_by_devices['month_year'] = trend_by_devices['month_year'].dt.strftime('%d.%m.%Y')

        #Save as Excel
        trend_by_devices_path = self.output_path+'trend_by_devices.xlsx'
        writer = pd.ExcelWriter(trend_by_devices_path,engine='xlsxwriter')
        data = trend_by_devices.to_excel(writer, sheet_name = 'Лист 1', index = False)
        writer.save()

    #=================== TRAFFIC SOURCES ===================
    def traffic_sources(self):
        temp = []

        #first_month = (datetime.date.today() - relativedelta(months=6)).strftime('%b')
        #last_month = datetime.date.today().strftime('%b')
        first_month = 'Mar'
        last_month = 'Sep'
        year = datetime.date.today().strftime('%Y')

        for i in traffic_sources_list:
            filename = self.downloads_path+'Traffic Sources by Type (domain='+i+', range='+first_month+ \
                        ' '+year+' – '+last_month+' '+year+').csv'
            df = pd.read_csv(filename, sep = ",")
            df.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
            df['Domain'] = i
            df.columns = df.columns.str.lower()
            temp.append(df)

        traffic_sources = pd.concat(temp, axis = 0, ignore_index = True)
        traffic_sources.fillna(0, inplace = True)

        traffic_sources = pd.merge(traffic_sources, domains,on="domain",how="left")

        #Month = Mon + Year
        traffic_sources['year'] = (pd.DatetimeIndex(traffic_sources['month']).year).astype("string")

        traffic_sources['month'] = traffic_sources['month_number'] = pd.DatetimeIndex(traffic_sources['month']).month
        traffic_sources['month_number'] = traffic_sources['month_number'].astype("string")
        traffic_sources['month'] = traffic_sources['month_number'].apply(lambda x: (datetime.datetime.strptime(x, "%m")
                                                                                   ).strftime("%b"))

        #traffic_sources['month'] = traffic_sources['month'].apply(lambda x: calendar.month_abbr[x])
        #traffic_sources['month_number'] = traffic_sources['month'].apply(lambda x: datetime.datetime.strptime(x, "%b").month)

        traffic_sources['month_year'] = (pd.to_datetime(traffic_sources['month_number'] + ' ' + traffic_sources['year'])
                                        ).dt.strftime('%d.%m.%Y')

        #traffic_sources['month_year'] = pd.to_datetime(traffic_sources['month_year'])
        #traffic_sources['month_year'] = traffic_sources['month_year'].dt.strftime('%d.%m.%Y')

        #Save as Excel
        traffic_sources_path = self.output_path+'traffic_sources.xlsx'
        writer = pd.ExcelWriter(traffic_sources_path,engine='xlsxwriter')
        data = traffic_sources.to_excel(writer, sheet_name = 'Лист 1', index = False)
        writer.save()

    #=================== JOURNEY SOURCES ===================
    def journey_sources(self):
        temp_count = 1
        journey_temp = []

        for x in month_list:
            #domains = pd.read_csv('C:/Users/gerber.l/Downloads/domains.csv', sep = ';')

            last_month = (datetime.date.today() - relativedelta(months=temp_count+1)).strftime('%b')
            #last_month = 'Aug'
            year = datetime.date.today().strftime('%Y')

            for i in globals()['journey_list_%s' % x]:
                filename = self.downloads_path+'All Sources (date='+last_month+' '+year+', target='+i+').csv'
                df = pd.read_csv(filename, sep = ",")
                #df.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
                df.columns = df.columns.str.lower()
                df['domain'] = i
                df['month'] = x
                df['year'] = year
                journey_temp.append(df)

            temp_count += 1

        journey_sources = pd.concat(journey_temp, axis = 0, ignore_index = True)
        journey_sources.fillna(0, inplace = True)

        journey_sources = pd.merge(journey_sources, domains,on="domain",how="left")

        #Month = Mon
        journey_sources['year'] = journey_sources['year'].astype("string")

        journey_sources['month_number'] = journey_sources['month'].apply(lambda x: datetime.datetime.strptime(x, "%b").month)
        journey_sources['month_number'] = journey_sources['month_number'].astype("string")
        journey_sources['month_year'] = (pd.to_datetime(journey_sources['month_number'] + ' ' + journey_sources['year'])).dt.strftime('%d.%m.%Y')

        #Save as Excel
        journey_sources_path = self.output_path+'journey_sources.xlsx'
        writer = pd.ExcelWriter(journey_sources_path,engine='xlsxwriter')
        data = journey_sources.to_excel(writer, sheet_name = 'Лист 1', index = False)
        writer.save()

    #=================== TRAFFIC BY COUNTRIES ===================
    def traffic_by_countries(self): 
        countries = pd.read_csv('C:/Users/semrush files/countries.csv', 
                                engine="python", 
                                encoding="cp1251", 
                                sep=';', 
                                quotechar='"', 
                                error_bad_lines=False)
        countries.rename(columns = {'short':'country'}, inplace = True)

        temp_count = 1
        traffic_temp = []

        for x in self.month_list:
            #domains = pd.read_csv('C:/Users/Downloads/domains.csv', sep = ';')

            last_month = (datetime.date.today() - relativedelta(months=temp_count+1)).strftime('%b')
            #last_month = 'Aug'
            year = datetime.date.today().strftime('%Y')

            traffic_1 = pd.read_csv(self.downloads_path+'Traffic by Country (date='+str(last_month)\ 
                                    +' '+str(year)+', geoType=country).csv', sep = '","|""|,|"')
            traffic_1 = traffic_1[traffic_1.columns.drop(list(traffic_1.filter(regex='Unnamed')))]
            traffic_1.columns = traffic_1.columns.str.lower()
            traffic_1['domain'] = globals()['traffic_by_countries_list_%s' % x][0]
            traffic_1['month'] = x
            traffic_1['year'] = year
            traffic_temp.append(traffic_1)

            for i in range(1, self.domain_list[-1]):
                traffic_by_countries_name = self.downloads_path+'Traffic by Country (date=' \
                +str(last_month)+' '+str(year)+', geoType=country) ('+str(i)+').csv'
                traffic_by_countries = pd.read_csv(traffic_by_countries_name, sep = '","|""|,|"')
                traffic_by_countries = traffic_by_countries[traffic_by_countries.columns.drop(
                    list(traffic_by_countries.filter(regex='Unnamed')))]
                traffic_by_countries['Domain'] = globals()['traffic_by_countries_list_%s' % x][i]
                traffic_by_countries['Month'] = x
                traffic_by_countries['Year'] = year
                traffic_by_countries.columns = traffic_by_countries.columns.str.lower()
                traffic_temp.append(traffic_by_countries)

            temp_count += 1

        traffic_concat = pd.concat(traffic_temp, axis = 0, ignore_index = True)   

        traffic_countries = pd.merge(traffic_concat, countries,on="country",how="left")
        traffic_countries['bounce rate'] = traffic_countries['bounce rate'].str.rstrip("%").astype(float)

        traffic_countries['traffic_no_bounce'] = round((traffic_countries['traffic'] \
                                                        - ((traffic_countries['traffic'] \
                                                            * traffic_countries['bounce rate']) / 100)).astype(float))
        traffic_countries['traffic_bounce'] = round(((traffic_countries['traffic'] \
                                                      * traffic_countries['bounce rate']) / 100).astype(float))

        traffic_countries['desktop share'] = traffic_countries['desktop share'].apply(
                                                lambda x : '0%' if str(x) == '<\xa00.01%' else x)
        traffic_countries['mobile share'] = traffic_countries['mobile share'].apply(
                                                lambda x : '0%' if str(x) == '<\xa00.01%' else x)

        traffic_countries['desktop share'] = traffic_countries['desktop share'].str.rstrip("%").astype(float)
        traffic_countries['mobile share'] = traffic_countries['mobile share'].str.rstrip("%").astype(float)

        traffic_countries['desktop'] = round(((traffic_countries['unique visitors'] \
                                               * traffic_countries['desktop share']) / 100).astype(float))
        traffic_countries['mobile'] = round(((traffic_countries['unique visitors'] \
                                              * traffic_countries['mobile share']) / 100).astype(float))

        traffic_countries = pd.merge(traffic_countries, domains,on="domain",how="left")

        #Month = Mon
        traffic_countries['year'] = traffic_countries['year'].astype("string")
        traffic_countries['month_number'] = traffic_countries['month'] = traffic_countries['month'].apply(
                                            lambda x: datetime.datetime.strptime(x, "%b").month)
        traffic_countries['month_number'] = traffic_countries['month_number'].astype("string")
        traffic_countries['month'] = traffic_countries['month_number'].apply(
                                     lambda x: (datetime.datetime.strptime(x, "%m")).strftime("%b"))
        #traffic_countries['month'] = traffic_countries['month'].apply(lambda x: calendar.month_abbr[x])

        traffic_countries['month_year'] = (pd.to_datetime(traffic_countries['month_number'] \
                                                          + ' ' + traffic_countries['year'])).dt.strftime('%d.%m.%Y')

        countries_ru_list = traffic_countries['name'].drop_duplicates()
        countries_en_list = traffic_countries['english'].drop_duplicates()
        countries_location_ru_list = traffic_countries['location'].drop_duplicates()
        calendar = traffic_countries['month_year'].drop_duplicates()

        #Save as Excel (traffic_countries)
        traffic_countries_path = self.output_path+'traffic_countries.xlsx'
        writer = pd.ExcelWriter(traffic_countries_path,engine='xlsxwriter')
        data = traffic_countries.to_excel(writer, sheet_name = 'Лист 1', index = False)
        writer.save()

        #Save as Excel (countries_ru_list)
        countries_ru_path = self.output_path+'countries_ru_list.xlsx'
        writer = pd.ExcelWriter(countries_ru_path,engine='xlsxwriter')
        data = countries_ru_list.to_excel(writer, sheet_name = 'Лист 1', index = True)
        writer.save()

        #Save as Excel (countries_en_list)
        countries_en_path = self.output_path+'countries_en_list.xlsx'
        writer = pd.ExcelWriter(countries_en_path,engine='xlsxwriter')
        data = countries_en_list.to_excel(writer, sheet_name = 'Лист 1', index = True)
        writer.save()

        #Save as Excel (countries_location_ru_list)
        countries_location_ru_path = self.output_path+'countries_location_ru_list.xlsx'
        writer = pd.ExcelWriter(countries_location_ru_path,engine='xlsxwriter')
        data = countries_location_ru_list.to_excel(writer, sheet_name = 'Лист 1', index = True)
        writer.save()

        #Save as Excel (calendar)
        calendar_self.output_path = self.output_path+'calendar.xlsx'
        writer = pd.ExcelWriter(calendar_self.output_path,engine='xlsxwriter')
        data = calendar.to_excel(writer, sheet_name = 'Лист 1', index = True)
        writer.save()

    #=================== COMPANY & DOMAINS ===================
    def domains_company(self):
        domains = pd.read_csv('C:/Users/Semrush/domains.csv', sep = ';')
        domains['domain'] = domains['domain'].apply(
                            lambda x: ((str(x).replace('https://www.', '')
                                       ).replace('https://', '')).replace('/', ''))
        domains = domains.drop_duplicates()
        company = domains['company'].drop_duplicates()
        domains = domains['domain']

        temp_domains = domains.loc[self.domain_list[0]:(self.domain_list[-1] - 1)]
        temp_company = company.loc[self.domain_list[0]:(self.domain_list[-1] - 1)]

        #Save as Excel
        domains_list_path = self.output_path+'domains_list.xlsx'
        writer = pd.ExcelWriter(domains_list_path,engine='xlsxwriter')
        data = temp_domains.to_excel(writer, sheet_name = 'Лист 1', index = True)
        writer.save()

        #Save as Excel
        company_list_path = self.output_path+'company_list.xlsx'
        writer = pd.ExcelWriter(company_list_path,engine='xlsxwriter')
        data = temp_company.to_excel(writer, sheet_name = 'Лист 1', index = True)
        writer.save()

        
#=================== PREPROCESSING ===================
url = 'URL_to_WebSite'
driver_path = 'C:/DRIVER_PATH_.exe'

#=================== CHOOSE MONTH ===================
month_list_choose = ['Other number', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

month_list = []
number_list = []
  
number = input('Enter the number of the month, without a space, separated by a comma: ')
number_list.append(number)
number_list = [int(x) for xs in number_list for x in xs.split(',')]

number_list = list(set(number_list))
for i in number_list:
    month_list.append(month_list_choose[i])
    
print('Choosed month: ', month_list)

#=================== AMOUNT CHOOSING ===================
def_amount = int(input('Enter number of domains: '))
def_start = int(input('Enter first domain: '))
def_end = def_start + def_amount

print('Last domain: ', def_end)

#month_list = ['Aug', 'Jul', 'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan']
#month_list = ['Aug', 'Jul']

for x in month_list:
    globals()['traffic_by_countries_list_%s' % x] = []
    
for x in month_list:
    globals()['journey_list_%s' % x] = []

#backlinks_anchors_list = []
#backlinks_refdomains_list = []

visits_list = []
unique_list = []
duration_list = []
bounce_rate_list = []

traffic_sources_list = []
journey_list = []
traffic_by_countries_list = []

#def_amount = 100
#def_start = 526
#def_end = 626

#=================== FUNCTION ===================
df = downloader_prepare('login', 'password', 'demo_domain', driver_path, 'www.google.com', url, download_path)

#=================== DOMAINS ===================
domains = pd.read_csv('C:/PATH_TO_domains.csv', sep = ';')
domains['domain'] = domains['domain'].apply(lambda x: (
                    (str(x).replace('https://www.', '')
                    ).replace('https://', '')).replace('/', ''))
domains = domains.drop_duplicates()

downloads_path = r"C:/Users/Semrush/Downloads/"
output_path = r"C:/Users/Semrush/Output/"

#=================== OUTPUT ===================

if __name__ == '__main__':
    #preprocessing('downloads_path', 'output_path', month_list[0], month_list[-1]).overview()
    #preprocessing('downloads_path', 'output_path', month_list[0], month_list[-1]).backlinks_anchors()
    #preprocessing('downloads_path', 'output_path', month_list[0], month_list[-1]).backlinks_refdomains()
    preprocessing('downloads_path', 'output_path', month_list[0], month_list[-1]).trend_by_devices()
    preprocessing('downloads_path', 'output_path', month_list[0], month_list[-1])traffic_sources()
    preprocessing('downloads_path', 'output_path', month_list[0], month_list[-1])journey_sources()
    preprocessing('downloads_path', 'output_path', month_list[0], month_list[-1])traffic_by_countries()
    preprocessing('downloads_path', 'output_path', month_list[0], month_list[-1])domains_company()

