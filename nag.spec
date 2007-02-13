Summary:	LDP Network Administrator's Guide
Summary(de.UTF-8):	LDP-Netzwerk-Administrator-Handbuch
Summary(fr.UTF-8):	Guide de l'administrateur réseau du LDP
Summary(pl.UTF-8):	Podręcznik Administratora Sieci LDP
Summary(tr.UTF-8):	LDP - NAG, Ağ yöneticisinin el kitabı
Name:		nag
Version:	2.0
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}-%{version}.html.tar.gz
# Source0-md5:	450a4f706f24da3cc654867d36872c7f
URL:		http://www.tldp.org/LDP/nag2/
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a generic guide to the Network Administration of Linux
systems. Check http://www.tldp.org/ for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l fr.UTF-8
Guide générique à l'administration réseau sous Linux. Allez sur
http://www.tldp.org/ pour plus d'informations sur le Projet de
Documentation Linux (LDP) et les mises à jour éventuelles de cette
version.

%description -l de.UTF-8
Dies ist eine allgemeine Anleitung zur Netzwerkverwaltung von
Linux-Systemen. Unter http://www.tldp.org/ finden Sie weitere
Informationen über das Linux Documentation Project und ggf. Updates zu
dieser Version.

%description -l pl.UTF-8
To jest ogólny przewodnik po Administracji Sieciami Linuksowymi.
Więcej informacji na temat Projektu Dokumentacji Linuksa (LDP) oraz
uaktualnienia tego dokumentu możesz znaleźć pod adresem
<http://www.tldp.org/>.

%description -l tr.UTF-8
Bu kitap, LDP (Linux belgeleme çalışması) sonucunda ortaya çıkan
eserlerden biri. Serinin diğer kitapları ile birlikte bu kitapların
güncel bir yansısına http://www.tldp.org/ altından erişebilirsiniz. Ağ
yöneticisinin el kitabı Linux'da ağ hizmetlerinin yönetimi üzerine
genel bilgileri içerir.

%prep
%setup -q -n %{name}2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/nag
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/nag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/nag
