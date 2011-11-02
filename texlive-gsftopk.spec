Name:		texlive-gsftopk
Version:	1.19.2
Release:	1
Summary:	Convert "ghostscript fonts" to PK files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/gsftopk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gsftopk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gsftopk.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-gsftopk.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Designed for use with xdvi and dvips this utility converts
Adobe Type 1 fonts to PK bitmap format. It should not
ordinarily be much used nowadays, since both its target
applications are now capable of dealing with Type 1 fonts,
direct.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdir}/dvips/gsftopk/render.ps
%doc %{_mandir}/man1/gsftopk.1*
%doc %{_texmfdir}/doc/man/man1/gsftopk.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
