IndexAbbrMapping= {
    'SDP':'001',
    'PRD':'002',
    'SDD':'003',
    'STR':'004',
}
def GetDocIndeStrByDocAbbr(docAbbr):
    return IndexAbbrMapping.get(docAbbr,'')
