 cat a.txt | xargs -I{} wkdict {} > wkdict_generate.md
 
 cat a.txt | xargs -I{} swift test.swift {} > mac_gen.md