#Code, that fills the up the jupyter notebook too much

class describeMultiIndex:

    
    def __init__(self, DataFrame):
        self.columns = DataFrame.columns
        self.shape = DataFrame.shape
        self.index = DataFrame.index
        
    def render(self):
        indexList = '''<h3>A short overview of the MultiIndex in the DataFrame</h3>
                    <ol start=\'0\' type=\'1\'>
                    '''
        import re
        regEx = re.compile('\(.*?\)')
        for l in self.columns.levels:
            indexList += '<li =\'1\'>{0} ('.format(l.name)
            itemCount = len(l)
            
            if itemCount<4:
                    for i in range(itemCount):
                        if i < itemCount-1:
                            s = re.sub(regEx, '', re.sub(',',' &ndash;',l[i]))
                            indexList += '{0}, '.format(s)
                        else:
                            s = re.sub(regEx, '', re.sub(',',' &ndash;',l[i]))                            
                            indexList += '{0})'.format(s)
            elif len(l)>3:
                    s1 = re.sub(regEx, '', re.sub(',',' &ndash;',l[0]))
                    s2 = re.sub(regEx, '', re.sub(',',' &ndash;',l[-1]))
                    indexList += '{0} &hellip; {1} [{2}])'.format(s1, s2, len(l))

        indexList += '</ol>'
        return indexList


        
    
        