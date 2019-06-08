IndexAbbrMapping= {
    'SDP':'001',
    'SRS':'002',
    'SDD':'003',
    'STR':'004',
}
def GetDocIndeStrByDocAbbr(docAbbr):
    return IndexAbbrMapping.get(docAbbr,'')
