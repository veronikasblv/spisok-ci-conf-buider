require 'yaml'

print("bebra\n")
procmeta = YAML::load_file(File::join('../sections', 'p.yml'))
procmeta['sections'].map do |f|
    print(f)
end
print(procmeta['sections'])