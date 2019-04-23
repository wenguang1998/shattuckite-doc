function(ShattuckiteSphinxDoc aDocAbbr aDocIndex aSphinxRoot aOutDir )
  message(STATUS "Add Document: shattuckite-${aDocAbbr} : ${aSphinxRoot}" )
  file(GLOB_RECURSE ${aDocAbbr}_DEPENDENCIES 
        ${aSphinxRoot}/*.rst
        ${aSphinxRoot}/*.rstinc
        ${aSphinxRoot}/*.uml
        ${aSphinxRoot}/*.json
        ${aSphinxRoot}/*.dot)

  execute_process (
      COMMAND bash -c "git log --grep \"SHADOC-${aDocIndex}\" | head -n 1| cut -d' ' -f2"
      OUTPUT_VARIABLE ${aDocAbbr}_LATESTDIGEST
  )
  string(REPLACE "\n" "" ${aDocAbbr}_LATESTDIGEST ${${aDocAbbr}_LATESTDIGEST})

  execute_process (
      COMMAND git describe --match "*-${aDocAbbr}"  ${${aDocAbbr}_LATESTDIGEST}
      OUTPUT_VARIABLE ${aDocAbbr}_VERSION
  )
  string(REPLACE "\n" "" ${aDocAbbr}_VERSION ${${aDocAbbr}_VERSION})

  set(tDynamicOutName ${aOutDir}/shattuckite-${${aDocAbbr}_VERSION}.pdf)
  set(tStaticOutName ${aOutDir}/shattuckite-${aDocAbbr}.pdf)

  add_custom_command(OUTPUT ${aOutDir}/${aDocAbbr}_BUILDINGFLAG
    COMMAND git describe --match "*-${aDocAbbr}" > ${aOutDir}/${aDocAbbr}_BUILDINGFLAG
  )
  
  add_custom_command(OUTPUT ${tStaticOutName}
    COMMAND make latexpdf
    COMMAND cp ./build/latex/shattuckite-${aDocAbbr}.pdf ${tDynamicOutName}
    COMMAND cp ./build/latex/shattuckite-${aDocAbbr}.pdf ${tStaticOutName}
    WORKING_DIRECTORY ${aSphinxRoot}
    DEPENDS ${${aDocAbbr}_DEPENDENCIES} 
    MAIN_DEPENDENCY ${aOutDir}/${aDocAbbr}_BUILDINGFLAG
  )

  add_custom_command(OUTPUT shattuckite-${aDocAbbr}-html
    COMMAND make html
    COMMAND cp -r  ./build/html  ${aOutDir}/${aDocAbbr}-html 
    WORKING_DIRECTORY ${aSphinxRoot}
    DEPENDS ${${aDocAbbr}_DEPENDENCIES}
    MAIN_DEPENDENCY ${aOutDir}/${aDocAbbr}_BUILDINGFLAG
  )

endfunction(ShattuckiteSphinxDoc)