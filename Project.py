#!/usr/bin/env python
# coding: utf-8

# 1.a 
# 
# My file contains information regarding country, unemployment rate as a percentage, GDP per capita in US dollars, government type, and population.
#     
# I want to design a program that reads a file of containing the Country name, GDP per capita, and Government type.

# 1.b
# 
# I want my program to produce a forecast of the GDP per capita compared to unemployment rate of only countries governed under a republic system of government with unemployment under a certain number. I do not care about which countries and their names exactly, only the correlation between unemployment rate and GDP per capita. Country names are used only for initial identification of what countries I will be comparing.
# 
# The output type will most likely be a scatterplot representing the X axis as a list of unemployment rates and the Y axis as the GDP per capita at a certain unemployment rate. The countries chosen must adhere to my set parameters. (republic government type and unemployment under a certain percentage)

# 1.c 
# 
# expect(main('country_per_cap_gdp_unemployment_gov_type_pop.csv'),[C1,C2,C4])
# expect(main('country_per_cap_gdp_unemployment_gov_type_pop.csv'), ['Bolivia, 7.4, 6630, 'Republic'])
#          
#      |       x
#      |    x      x
#      |  x  x  x
#   gdp|x  x
#      |                                 a sample of what a graph might look like, (not based on example tst function above)
#      |      x     x
#      |_____________________
#            Unemployment rate

# In[1]:


from cs103 import *
from typing import NamedTuple, List

Country = NamedTuple ('Country', [('name', str),
                                  ('unemployment_rate', int),
                                  ('gdp_per_cap', int),
                                  ('gov_type', str)])
#interp. a country with country name, unemployment rate, gdp per capita, and government type

C1 = Country('Estonia', 6.3, 28095, 'Republic')
C2 = Country('China', 4.1, 14107, 'Communist state')
C3 = Country('Finland', 9.1, 40601, 'Republic')
C4 = Country('United Kingdom', 4.9, 41325, 'Constitutional monarchy')
C5 = Country('Bolivia', 7.4, 6630, 'Republic')
C6 = Country('Bosnia and Herzegovina', 35, 10427, 'Republic')

def fn_for_country(c: Country) -> ...: #template based on compound
    return...(c.name,
              c.unemployment_rate,
              c.gpd_per_cap,
              c.gov_type)


#List[Country]
#interp. a list of countries

L0 = []
L1 = [C1]
L2 = [C1, C2, C3]
L3 = [C1, C2, C3, C4, C5, C6] #only used for the scatter plot

#template based on arbitrary-sized
def fn_for_loc(loc: List[Country]) -> ...:
    # description of the acc
    acc = ... # type: ...
    for t in lot:
        acc = ...(fn_for_country(c), acc)
    return ...(acc)


# In[2]:


import csv
import matplotlib.pyplot as plt

def main(filename: str) -> Optional[str]:
    """
    Reads information from given filename and returns a scatterplot of gross domestic production (GDP) of
    countries under a Republic system of government with a unemployment rate below a certain percentage
    
    """
    # return None #body of the stub
    # template as a function composition
    return plot_scatterplot(read(fn))

def unemployment_is_valid(ur: Optional[int]) -> bool:
    """
    return True if unemployment rate is an int and False otherwise
    """
    #return True #stub
    #template from Optional
    if ur is None:
        return False
    else:
        return True

def gdp_is_valid(gdp: Optional[int]) -> bool:
    """
    return True if gross domestic production is an int and False otherwise
    """
    #return True #stub
    #template from Optional
    if gdp is None:
        return False
    else:
        return True

def read(fn: str) -> List[Country]:
    """    
    reads information from the specified file and returns a list of countries
    """
    #return [] #stub
    #template form htDAP
   
    # loc contains the result so far
    loc = [] # type: List[Country]

    with open(fn, encoding = "ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader) # skip header line
        for row in reader:
            country_name = (row[1])
            unemployment_rate = parse_float(row[2])
            gross_domestic_production = parse_int(row[3])
            government_type = (row[4])
            if unemployment_is_valid(unemployment_rate) and gdp_is_valid(gross_domestic_production):
                c = Country(country_name,
                            unemployment_rate,
                            gross_domestic_production,
                            government_type)
                loc.append(c)
    return loc


def is_republic(loc: List[Country]) -> List[Country]:
    '''
    takes a list of countries and returns a list of only republic countries
    '''
    #return [] #body of the stub
    #template form List[Country]
    
    #republic_countries contains only republic government countries seen so far
    republic_countries = [] #type: List[Country]
    for c in loc:
        if c.gov_type == 'Republic': #Only adds countries with Republic governments
            republic_countries.append(c)
    return republic_countries
    
    #sets a ceiling for maximum unemployment rate allowed
def ceiling_unemployment_rate(c: Country) -> bool: 
    '''
    takes a list of countries and returns true if the unemployment rate is below a certain percentage
    '''
    #return True #stub
    #template from fn_for_country
    return c.unemployment_rate <= 9

    #sets a floor for minimum unemployment rate allowed
def floor_unemployment_rate(c: Country) -> bool:
    '''
    takes a list of countries and returns true if the unemployment rate is above a certain percentage
    '''
    #return True #stub
    #template from fn_for_country
    return c.unemployment_rate >= 2
    
def list_unemployment_rate(loc: List[Country]) -> List[float]:
    '''
    takes a list of countries and returns a list of country names
    '''
    #return [] #stub
    #template from List[Country]
    
    #country_name contains country names seen so far
    unemployment_rate = [] #type: List[str]
    for c in loc:
        unemployment_rate.append(c.unemployment_rate)
    return unemployment_rate
    
        
def list_gdp(loc: List[Country]) -> List[int]:
    '''
    takes a list of countries and returns a list of gdp per capita
    '''
    #return [] #stub
    #template from List[Country]
    
    #gdp contains a list of countries gdp seen so far
    gdp = [] #type: List[int]
    for c in loc:
        gdp.append(c.gdp_per_cap)
    return gdp

def plot_scatterplot(loc: List[Country]) -> None:
    """
    displays a scatterplot of gdp per capita in loc by country
    """
    #return None #body of the stub
    
    # set the labels for the axes
    plt.xlabel('Unemployment rate (%)')
    plt.ylabel('GDP Per Capita (in USD)')
    plt.title('GDP Per Capita Compared to Unemployment Rate')

    # range for the axes
    # [x-min, x-max, y-min, y-max]
    plt.axis([0.0 ,10.0 ,10000,50000])

    unemployment_rate = list_unemployment_rate(loc)
    gdp = list_gdp(loc)
    
    # creates the scatterplot, with markers that are red (c='r') and triangular (marker='^')
    plt.scatter(unemployment_rate, gdp, marker='x', c='r', s=15)
    plt.grid(True)

    # show the plot
    plt.show()
    
    return None

#begins testing
start_testing()

# no examples and tests for main since it's drawing a scatterplot and returning None

#examples and tests for read
expect(read('countries_gdp_and_unemployment_test1.csv'), [C1, C2, C3, C4])
expect(read('countries_gdp_and_unemployment_test2.csv'), [C5, C6, C2])

#examples and tests for is_republic
expect(is_republic(L0), [] )
expect(is_republic(L1), [C1])
expect(is_republic(L2), [C1, C3])

#examples and tests for ceiling_unemployment_rate
expect(ceiling_unemployment_rate(C2), True )
expect(ceiling_unemployment_rate(C3), False )
expect(ceiling_unemployment_rate(C5), True )

#examples and tests for floor_unemployment_rate
expect(floor_unemployment_rate(C2), True )
expect(floor_unemployment_rate(C3), True )
expect(floor_unemployment_rate(C5), True )

#examples and tests for list_unemployment_rate
expect(list_unemployment_rate(L1), [6.3] )
expect(list_unemployment_rate(L2), [6.3, 4.1, 9.1])

#examples and tests for list_gdp
expect(list_gdp(L1), [28095])
expect(list_gdp(L2), [28095, 14107, 40601])

#examples and tests for plot_scatterplot
expect(plot_scatterplot(L3), None)

#finishes testing and prints summary
summary()


# In[ ]:




