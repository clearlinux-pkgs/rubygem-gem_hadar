#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-gem_hadar
Version  : 1.2.1
Release  : 5
URL      : https://rubygems.org/downloads/gem_hadar-1.2.1.gem
Source0  : https://rubygems.org/downloads/gem_hadar-1.2.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-gem_hadar
BuildRequires : rubygem-rdoc

%description


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n gem_hadar-1.2.1
gem spec %{SOURCE0} -l --ruby > rubygem-gem_hadar.gemspec

%build
gem build rubygem-gem_hadar.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
gem_hadar-1.2.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/gem_hadar-1.2.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/RvmConfig/cdesc-RvmConfig.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/RvmConfig/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/TemplateCompiler/cdesc-TemplateCompiler.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/TemplateCompiler/compile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/TemplateCompiler/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/TemplateCompiler/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/ask%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/build_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/cdesc-GemHadar.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/clean-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/clobber-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/compile_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/create_all_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/default_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/dependency-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/development_dependency-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/doc_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/gem_push_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/gems_install_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/gemspec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/gemspec_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/git_remote-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/has_to_be_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/ignore-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/install_library-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/install_library_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/master_push_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/package_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/rcov_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/require_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/rvm-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/rvm_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/spec_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/start_simplecov-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/test_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/version_bump_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/version_push_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/version_tag_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/version_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/write_gemfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/GemHadar/write_ignore_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/Object/GemHadar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/Object/template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/gem_hadar-1.2.1/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/VERSION
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/gem_hadar.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/lib/gem_hadar.rb
/usr/lib64/ruby/gems/2.2.0/gems/gem_hadar-1.2.1/lib/gem_hadar/version.rb
/usr/lib64/ruby/gems/2.2.0/specifications/gem_hadar-1.2.1.gemspec
