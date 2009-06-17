# TODO:
# - make jruby.sh work with our paths
# - package all scripts
Summary:	JRuby - A Java implementation of the Ruby language
Summary(pl.UTF-8):	JRuby - implementacja języka Ruby w Javie
Name:		jruby
Version:	0.9.0
Release:	0.1
License:	CPL or GPL or LGPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/jruby/%{name}-src-%{version}.tar.gz
# Source0-md5:	0e5a764dc16b018624e7a57939d64d7e
URL:		http://jruby.sourceforge.net/
BuildRequires:	ant
BuildRequires:	jdk >= 1.4
Requires:	jre >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JRuby is the effort to recreate the Ruby (http://www.ruby-lang.org/)
interpreter in Java.

The Java version is be tightly integrated with Java to allow both to
script any Java class and to embed the interpreter into any Java
application.

%description -l pl.UTF-8
JRuby to próba odtworzenia interpretera języka Ruby
(http://www.ruby-lang.org/) w Javie.

Wersja w Javie jest ściśle zintegrowana z Javą aby umożliwić zarówno
używanie dowolnej klasy Javy w skrypcie, jak i osadzać interpreter w
dowolnej aplikacji w Javie.

%prep
%setup -q

%build
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_bindir}}

install bin/jruby $RPM_BUILD_ROOT%{_bindir}/jruby
install lib/jruby.jar $RPM_BUILD_ROOT%{_javadir}/jruby-%{version}.jar
ln -s jruby-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jruby.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING COPYING.CPL README docs
%attr(755,root,root) %{_bindir}/jruby
%{_javadir}/jruby-%{version}.jar
%{_javadir}/jruby.jar
