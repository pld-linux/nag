Summary:	LDP Network Administrator's Guide
Summary(fr):	Guide de l'administrateur réseau du LDP
Summary(de):	LDP-Netzwerk-Administrator-Handbuch
Summary(pl):	Podrêcznik Administratora Sieci LDP
Summary(tr):	LDP - NAG, Að yöneticisinin el kitabý
Name:		nag
Version:	2.0
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}-%{version}.html.tar.gz
# Source0-md5:	450a4f706f24da3cc654867d36872c7f
URL:		http://www.tldp.org/LDP/nag2/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a generic guide to the Network Administration of Linux
systems. Check http://www.tldp.org/ for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l fr
Guide générique à l'administration réseau sous Linux. Allez sur
http://www.tldp.org/ pour plus d'informations sur le Projet de
Documentation Linux (LDP) et les mises à jour éventuelles de cette
version.

%description -l de
Dies ist eine allgemeine Anleitung zur Netzwerkverwaltung von
Linux-Systemen. Unter http://www.tldp.org/ finden Sie weitere
Informationen über das Linux Documentation Project und ggf. Updates zu
dieser Version.

%description -l pl
To jest ogólny przewodnik po Administracji Sieciami Linuksowymi. Wiêcej
informacji na temat Projektu Dokumentacji Linuksa (LDP) oraz
uaktualnienia tego dokumentu mo¿esz znale¼æ pod adresem
http://www.tldp.org/ .

%description -l tr
Bu kitap, LDP (Linux belgeleme çalýþmasý) sonucunda ortaya çýkan
eserlerden biri. Serinin diðer kitaplarý ile birlikte bu kitaplarýn
güncel bir yansýsýna http://www.tldp.org/ altýndan
eriþebilirsiniz. Að yöneticisinin el kitabý Linux'da að hizmetlerinin
yönetimi üzerine genel bilgileri içerir.

%prep
%setup -q -n nag2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LDP/nag

cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LDP/nag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/LDP/nag
