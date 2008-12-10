Summary:	Nebula - intrusion detection tool
Summary(pl.UTF-8):	Nebula - narzędzie do wykrywania włamań
Name:		nebula
Version:	0.2.3
Release:	0.1
License:	GPL v2
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/nebula/%{name}-%{version}.tar.bz2
# Source0-md5:	e6aa4c2c19c0aeec0563c6a1cc75b5e8
URL:		http://sourceforge.net/projects/nebula/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nebula automatically generates intrusion signatures from attack
traces. It runs as a daemon accepting attack submissions from
honeypots.

%description -l pl.UTF-8
Nebula automatycznie generuje sygnatury włamań na podstawie śladów
nieautoryzowanego dostępu. Pracuje w trybie demona przyjmując
informacje o atakach z honeypotów.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}client
