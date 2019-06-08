import logging
logger = logging.getLogger(__name__)


TemplateClassDiagram =\
"""@startuml
skinparam classAttributeIconSize 0

{classes}

{relation}

@enduml
"""

TemplateClass = \
    """
{abstractModifier} class {name}  {{
    {member}
    {method}
}}
"""

TemplateMember = "{visibilityModifier} {name}: {type} "
TemplateMethod = "{abstractModifier} {visibilityModifier} {type} {name}()"
TemplateRelation = '{superClass} {labelEnd} {modifier} {labelBegin} {baseClass} {labelMid}'

visibilityModifier = {
    "private": '-',
    "protected": "#",
    "packagePrivate": "~",
    "public": "+"
}

releationshipModifier = {
    "extension":  "<|--",
    "composition": "*--",
    "aggregation": "o--",
    "association": "--",
}


def getVisibilityModifier(verbose, default="public"):
    return visibilityModifier.get(verbose, visibilityModifier['public'])


def generateUMLClass(artObj, ofp):
    classList = []
    releationTupleList = []
    releationList = []

    tClassNameList = [i['name'] for i in artObj['class']]
    for tClass in artObj['class']:
        classList.append(
            TemplateClass.format(
                abstractModifier= 'abstract' if tClass.get('abstract') else 'interface' if tClass.get('interface') else '',

                member="\n".join([TemplateMember.format(
                    visibilityModifier=getVisibilityModifier(
                        i.get('accessibility')),
                    type=i.get('type', "any"),
                    name=i['name']) for i in tClass.get('member', [])]),

                method="\n".join([TemplateMethod.format(
                    abstractModifier=r"{abstract}" if i.get(
                        'abstract', False) else r"{static}" if i.get('static', False) else '',
                    visibilityModifier=getVisibilityModifier(
                        i.get('accessibility')),
                    type=i.get('type', 'any'),
                    name=i.get('name', "None")) for i in tClass['method']]),
                name=tClass['name']
            )
        )
        # Handle UML extension
        if tClass.get("extension") is not None:
            for superClass in tClass.get("extension"):
                releationList.append(TemplateRelation.format(
                    superClass=superClass,
                    labelEnd ='',
                    labelMid='',
                    labelBegin='',
                    baseClass=tClass['name'],
                    modifier =releationshipModifier['extension']
                ))

        for mem in tClass.get("member",[]):
            superClass =  mem.get('type')
            if  superClass in tClassNameList:
                releationShip = mem.get('UMLRelation')
                labelEnd = mem.get("UMLLabelEnd")
                labelBegin = mem.get("UMLLabelBegin")
                labelMid = mem.get("UMLLabelMid")

                # Handle UML composition and aggregation
                if releationShip == 'composition' or releationShip =='aggregation' or releationShip=='association':
                    releationList.append(TemplateRelation.format(
                        superClass=superClass,
                        labelEnd = '"{0}"'.format(labelEnd) if labelEnd is not None else '',
                        labelMid = ':{0}'.format(labelMid) if labelMid is not None else '',
                        labelBegin ='"{0}"'.format(labelBegin ) if labelBegin is not None else '',
                        baseClass=tClass['name'],
                        modifier =releationshipModifier[releationShip]
                    ))
                



    ofp.write(TemplateClassDiagram.format(
        classes="\n".join(classList),
        relation="\n".join(releationList)
    ))
