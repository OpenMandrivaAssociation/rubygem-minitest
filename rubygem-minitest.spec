%define	oname	minitest

Summary:	A small and fast replacement for ruby's huge and slow test/unit
Name:		rubygem-%{oname}
Version:	2.5.1
Release:	%mkrel 1
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	rubygem-hoe >= 2.5.0 rubygem-gemcutter >= 0.2.1
Requires:	rubygem-rubyforge >= 2.0.3
BuildArch:	noarch
Provides:	rubygem(%{oname}) = %{version}

%description
minitest/unit is a small and fast replacement for ruby's huge and slow
test/unit. This is meant to be clean and easy to use both as a regular test
writer and for language implementors that need a minimal set of methods to
bootstrap a working unit test suite. mini/spec is a functionally complete spec
engine. mini/mock, by Steven Baker, is a beautifully tiny mock object
framework. (This package was called miniunit once upon a time)

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}
chmod u+w -R %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
