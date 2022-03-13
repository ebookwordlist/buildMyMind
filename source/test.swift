#!/usr/bin/swift
import Foundation
if (CommandLine.argc < 2) {
    print("Usage: dictionary word")
}else{
    let argument = CommandLine.arguments[1]
    var result = DCSCopyTextDefinition(nil, argument as CFString, CFRangeMake(0, argument.count))?.takeRetainedValue() as String?
    print("\n\n") 
    result = result?.replacingOccurrences(of: "▸", with: "\n▸")
    result = result?.replacingOccurrences(of: ";", with: ";\n")
    print(result ?? "")
} 