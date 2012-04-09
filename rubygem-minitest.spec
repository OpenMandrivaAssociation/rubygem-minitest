# Generated from minitest-2.11.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	minitest

Summary:	minitest provides a complete suite of testing facilities supporting TDD, BDD, mocking, and benchmarking
Name:		rubygem-%{rbname}

Version:	2.12.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/seattlerb/minitest
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
minitest provides a complete suite of testing facilities supporting
TDD, BDD, mocking, and benchmarking.
"I had a class with Jim Weirich on testing last week and we were
allowed to choose our testing frameworks. Kirk Haines and I were
paired up and we cracked open the code for a few test
frameworks...
I MUST say that mintiest is *very* readable / understandable
compared to the 'other two' options we looked at. Nicely done and
thank you for helping us keep our mental sanity."
-- Wayne E. Seguin
minitest/unit is a small and incredibly fast unit testing framework.
It provides a rich set of assertions to make your tests clean and
readable.
minitest/spec is a functionally complete spec engine. It hooks onto
minitest/unit and seamlessly bridges test assertions over to spec
expectations.
minitest/benchmark is an awesome way to assert the performance of your
algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential
one!
minitest/mock by Steven Baker, is a beautifully tiny mock object
framework.
minitest/pride shows pride in testing and adds coloring to your test
output. I guess it is an example of how to write IO pipes too. :P
minitest/unit is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working
test suite. For example, there is no magic involved for test-case
discovery.
"Again, I can't praise enough the idea of a testing/specing
framework that I can actually read in full in one sitting!"
-- Piotr Szotkowski

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/hoe
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/hoe/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/minitest
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/minitest/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
