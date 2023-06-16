#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-igraph
Version  : 1.5.0
Release  : 71
URL      : https://cran.r-project.org/src/contrib/igraph_1.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/igraph_1.5.0.tar.gz
Summary  : Network Analysis and Visualization
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0+
Requires: R-igraph-lib = %{version}-%{release}
Requires: R-igraph-license = %{version}-%{release}
Requires: R-cli
Requires: R-cpp11
Requires: R-magrittr
Requires: R-pkgconfig
Requires: R-rlang
BuildRequires : R-cli
BuildRequires : R-cpp11
BuildRequires : R-magrittr
BuildRequires : R-pkgconfig
BuildRequires : R-rlang
BuildRequires : R-vdiffr
BuildRequires : buildreq-R
BuildRequires : gmp-dev
BuildRequires : libxml2-dev
BuildRequires : xz-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
handle large graphs very well and provides functions for generating
    random and regular graphs, graph visualization, centrality methods and
    much more.

%package lib
Summary: lib components for the R-igraph package.
Group: Libraries
Requires: R-igraph-license = %{version}-%{release}

%description lib
lib components for the R-igraph package.


%package license
Summary: license components for the R-igraph package.
Group: Default

%description license
license components for the R-igraph package.


%prep
%setup -q -n igraph
pushd ..
cp -a igraph buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686930589

%install
export SOURCE_DATE_EPOCH=1686930589
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-igraph
cp %{_builddir}/igraph/src/vendor/uuid/COPYING %{buildroot}/usr/share/package-licenses/R-igraph/16fd05e0c827f9372ff54c2a16b30353842a6df1 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/igraph/AUTHORS
/usr/lib64/R/library/igraph/CITATION
/usr/lib64/R/library/igraph/DESCRIPTION
/usr/lib64/R/library/igraph/INDEX
/usr/lib64/R/library/igraph/Meta/Rd.rds
/usr/lib64/R/library/igraph/Meta/demo.rds
/usr/lib64/R/library/igraph/Meta/features.rds
/usr/lib64/R/library/igraph/Meta/hsearch.rds
/usr/lib64/R/library/igraph/Meta/links.rds
/usr/lib64/R/library/igraph/Meta/nsInfo.rds
/usr/lib64/R/library/igraph/Meta/package.rds
/usr/lib64/R/library/igraph/Meta/vignette.rds
/usr/lib64/R/library/igraph/NAMESPACE
/usr/lib64/R/library/igraph/NEWS.md
/usr/lib64/R/library/igraph/R/igraph
/usr/lib64/R/library/igraph/R/igraph.rdb
/usr/lib64/R/library/igraph/R/igraph.rdx
/usr/lib64/R/library/igraph/benchmarks/correlated.R
/usr/lib64/R/library/igraph/benchmarks/local.scan.R
/usr/lib64/R/library/igraph/benchmarks/time_call.R
/usr/lib64/R/library/igraph/benchmarks/time_dirSelect.R
/usr/lib64/R/library/igraph/benchmarks/time_fr_layout.R
/usr/lib64/R/library/igraph/benchmarks/time_kk_layout.R
/usr/lib64/R/library/igraph/benchmarks/time_print.R
/usr/lib64/R/library/igraph/benchmarks/time_sgm.R
/usr/lib64/R/library/igraph/benchmarks/time_sir.R
/usr/lib64/R/library/igraph/demo/centrality.R
/usr/lib64/R/library/igraph/demo/cohesive.R
/usr/lib64/R/library/igraph/demo/community.R
/usr/lib64/R/library/igraph/demo/crashR.R
/usr/lib64/R/library/igraph/demo/hrg.R
/usr/lib64/R/library/igraph/demo/smallworld.R
/usr/lib64/R/library/igraph/doc/igraph.R
/usr/lib64/R/library/igraph/doc/igraph.Rmd
/usr/lib64/R/library/igraph/doc/igraph.html
/usr/lib64/R/library/igraph/doc/igraph_ES.R
/usr/lib64/R/library/igraph/doc/igraph_ES.html
/usr/lib64/R/library/igraph/doc/igraph_ES.rmd
/usr/lib64/R/library/igraph/doc/index.html
/usr/lib64/R/library/igraph/help/AnIndex
/usr/lib64/R/library/igraph/help/aliases.rds
/usr/lib64/R/library/igraph/help/igraph.rdb
/usr/lib64/R/library/igraph/help/igraph.rdx
/usr/lib64/R/library/igraph/help/paths.rds
/usr/lib64/R/library/igraph/html/00Index.html
/usr/lib64/R/library/igraph/html/R.css
/usr/lib64/R/library/igraph/html_library.license.terms
/usr/lib64/R/library/igraph/html_library.tcl
/usr/lib64/R/library/igraph/igraph.gif
/usr/lib64/R/library/igraph/igraph2.gif
/usr/lib64/R/library/igraph/my_html_library.tcl
/usr/lib64/R/library/igraph/tests/testthat.R
/usr/lib64/R/library/igraph/tests/testthat/_snaps/graph.bfs.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/graph.data.frame.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/hrg.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/make.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/old-data-type.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/plot/basic-graph-r-4-2.svg
/usr/lib64/R/library/igraph/tests/testthat/_snaps/print.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/serialize.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/utils-ensure.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/versions.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/vs-es-printing.md
/usr/lib64/R/library/igraph/tests/testthat/_snaps/vs-es.md
/usr/lib64/R/library/igraph/tests/testthat/celegansneural.gml.gz
/usr/lib64/R/library/igraph/tests/testthat/football.gml.gz
/usr/lib64/R/library/igraph/tests/testthat/helper.R
/usr/lib64/R/library/igraph/tests/testthat/power.gml.gz
/usr/lib64/R/library/igraph/tests/testthat/test-add.edges.R
/usr/lib64/R/library/igraph/tests/testthat/test-add.vertices.R
/usr/lib64/R/library/igraph/tests/testthat/test-adjacency.spectral.embedding.R
/usr/lib64/R/library/igraph/tests/testthat/test-all.st.cuts.R
/usr/lib64/R/library/igraph/tests/testthat/test-alpha.centrality.R
/usr/lib64/R/library/igraph/tests/testthat/test-are.connected.R
/usr/lib64/R/library/igraph/tests/testthat/test-arpack.R
/usr/lib64/R/library/igraph/tests/testthat/test-articulation.points.R
/usr/lib64/R/library/igraph/tests/testthat/test-as.directed.R
/usr/lib64/R/library/igraph/tests/testthat/test-as.undirected.R
/usr/lib64/R/library/igraph/tests/testthat/test-assortativity.R
/usr/lib64/R/library/igraph/tests/testthat/test-attributes.R
/usr/lib64/R/library/igraph/tests/testthat/test-authority.score.R
/usr/lib64/R/library/igraph/tests/testthat/test-average.path.length.R
/usr/lib64/R/library/igraph/tests/testthat/test-ba.game.R
/usr/lib64/R/library/igraph/tests/testthat/test-betweenness.R
/usr/lib64/R/library/igraph/tests/testthat/test-biconnected.components.R
/usr/lib64/R/library/igraph/tests/testthat/test-bipartite.projection.R
/usr/lib64/R/library/igraph/tests/testthat/test-bipartite.random.game.R
/usr/lib64/R/library/igraph/tests/testthat/test-bonpow.R
/usr/lib64/R/library/igraph/tests/testthat/test-bridges.R
/usr/lib64/R/library/igraph/tests/testthat/test-bug-1019624.R
/usr/lib64/R/library/igraph/tests/testthat/test-bug-1032819.R
/usr/lib64/R/library/igraph/tests/testthat/test-bug-1033045.R
/usr/lib64/R/library/igraph/tests/testthat/test-bug-1073705-indexing.R
/usr/lib64/R/library/igraph/tests/testthat/test-bug-1073800-clique.R
/usr/lib64/R/library/igraph/tests/testthat/test-bug-154.R
/usr/lib64/R/library/igraph/tests/testthat/test-canonical.permutation.R
/usr/lib64/R/library/igraph/tests/testthat/test-cliques.R
/usr/lib64/R/library/igraph/tests/testthat/test-closeness.R
/usr/lib64/R/library/igraph/tests/testthat/test-clusters.R
/usr/lib64/R/library/igraph/tests/testthat/test-coloring.R
/usr/lib64/R/library/igraph/tests/testthat/test-communities.R
/usr/lib64/R/library/igraph/tests/testthat/test-components.R
/usr/lib64/R/library/igraph/tests/testthat/test-constraint.R
/usr/lib64/R/library/igraph/tests/testthat/test-constructor-modifiers.R
/usr/lib64/R/library/igraph/tests/testthat/test-contract.vertices.R
/usr/lib64/R/library/igraph/tests/testthat/test-convex_hull.R
/usr/lib64/R/library/igraph/tests/testthat/test-correlated.R
/usr/lib64/R/library/igraph/tests/testthat/test-count.multiple.R
/usr/lib64/R/library/igraph/tests/testthat/test-decompose.graph.R
/usr/lib64/R/library/igraph/tests/testthat/test-degree.R
/usr/lib64/R/library/igraph/tests/testthat/test-degseq.R
/usr/lib64/R/library/igraph/tests/testthat/test-delete.edges.R
/usr/lib64/R/library/igraph/tests/testthat/test-delete.vertices.R
/usr/lib64/R/library/igraph/tests/testthat/test-deprecated_indexing_functions.R
/usr/lib64/R/library/igraph/tests/testthat/test-diameter.R
/usr/lib64/R/library/igraph/tests/testthat/test-dimSelect.R
/usr/lib64/R/library/igraph/tests/testthat/test-dominator.tree.R
/usr/lib64/R/library/igraph/tests/testthat/test-dot.product.game.R
/usr/lib64/R/library/igraph/tests/testthat/test-dyad.census.R
/usr/lib64/R/library/igraph/tests/testthat/test-edge.betweenness.R
/usr/lib64/R/library/igraph/tests/testthat/test-edge.betweenness.community.R
/usr/lib64/R/library/igraph/tests/testthat/test-edge.connectivity.R
/usr/lib64/R/library/igraph/tests/testthat/test-edgenames.R
/usr/lib64/R/library/igraph/tests/testthat/test-efficiency.R
/usr/lib64/R/library/igraph/tests/testthat/test-eulerian.R
/usr/lib64/R/library/igraph/tests/testthat/test-evcent.R
/usr/lib64/R/library/igraph/tests/testthat/test-farthest_vertices.R
/usr/lib64/R/library/igraph/tests/testthat/test-fastgreedy.community.R
/usr/lib64/R/library/igraph/tests/testthat/test-forestfire.R
/usr/lib64/R/library/igraph/tests/testthat/test-get.adjacency.R
/usr/lib64/R/library/igraph/tests/testthat/test-get.adjlist.R
/usr/lib64/R/library/igraph/tests/testthat/test-get.all.shortest.paths.R
/usr/lib64/R/library/igraph/tests/testthat/test-get.diameter.R
/usr/lib64/R/library/igraph/tests/testthat/test-get.edge.R
/usr/lib64/R/library/igraph/tests/testthat/test-get.edgelist.R
/usr/lib64/R/library/igraph/tests/testthat/test-get.incidence.R
/usr/lib64/R/library/igraph/tests/testthat/test-get.shortest.paths.R
/usr/lib64/R/library/igraph/tests/testthat/test-girth.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph-ids.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.adhesion.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.adjacency.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.adjlist.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.atlas.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.bfs.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.bipartite.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.complementer.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.compose.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.coreness.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.data.frame.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.de.bruijn.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.density.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.dfs.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.edgelist.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.eigen.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.isoclass.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.kautz.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.knn.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.maxflow.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.mincut.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.subisomorphic.lad.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph.subisomorphic.vf2.R
/usr/lib64/R/library/igraph/tests/testthat/test-graphNEL.R
/usr/lib64/R/library/igraph/tests/testthat/test-graphlets.R
/usr/lib64/R/library/igraph/tests/testthat/test-handler.R
/usr/lib64/R/library/igraph/tests/testthat/test-hrg.R
/usr/lib64/R/library/igraph/tests/testthat/test-hsbm.R
/usr/lib64/R/library/igraph/tests/testthat/test-identical_graphs.R
/usr/lib64/R/library/igraph/tests/testthat/test-igraph.options.R
/usr/lib64/R/library/igraph/tests/testthat/test-independent.vertex.sets.R
/usr/lib64/R/library/igraph/tests/testthat/test-index-es.R
/usr/lib64/R/library/igraph/tests/testthat/test-indexing.R
/usr/lib64/R/library/igraph/tests/testthat/test-indexing2.R
/usr/lib64/R/library/igraph/tests/testthat/test-indexing3.R
/usr/lib64/R/library/igraph/tests/testthat/test-is.bipartite.R
/usr/lib64/R/library/igraph/tests/testthat/test-is.chordal.R
/usr/lib64/R/library/igraph/tests/testthat/test-isomorphism.R
/usr/lib64/R/library/igraph/tests/testthat/test-iterators.R
/usr/lib64/R/library/igraph/tests/testthat/test-label.propagation.community.R
/usr/lib64/R/library/igraph/tests/testthat/test-laplacian.spectral.embedding.R
/usr/lib64/R/library/igraph/tests/testthat/test-largest.cliques.R
/usr/lib64/R/library/igraph/tests/testthat/test-largest.independent.vertex.sets.R
/usr/lib64/R/library/igraph/tests/testthat/test-layout.fr.R
/usr/lib64/R/library/igraph/tests/testthat/test-layout.kk.R
/usr/lib64/R/library/igraph/tests/testthat/test-layout.mds.R
/usr/lib64/R/library/igraph/tests/testthat/test-layout.merge.R
/usr/lib64/R/library/igraph/tests/testthat/test-layout.sugiyama.R
/usr/lib64/R/library/igraph/tests/testthat/test-layout_nicely.R
/usr/lib64/R/library/igraph/tests/testthat/test-layout_null_singleton.R
/usr/lib64/R/library/igraph/tests/testthat/test-leading.eigenvector.community.R
/usr/lib64/R/library/igraph/tests/testthat/test-leiden.R
/usr/lib64/R/library/igraph/tests/testthat/test-make.R
/usr/lib64/R/library/igraph/tests/testthat/test-make_graph.R
/usr/lib64/R/library/igraph/tests/testthat/test-make_lattice.R
/usr/lib64/R/library/igraph/tests/testthat/test-matching.R
/usr/lib64/R/library/igraph/tests/testthat/test-maximal_cliques.R
/usr/lib64/R/library/igraph/tests/testthat/test-minimal.st.separators.R
/usr/lib64/R/library/igraph/tests/testthat/test-minimum.size.separators.R
/usr/lib64/R/library/igraph/tests/testthat/test-modularity_matrix.R
/usr/lib64/R/library/igraph/tests/testthat/test-motifs.R
/usr/lib64/R/library/igraph/tests/testthat/test-multilevel.community.R
/usr/lib64/R/library/igraph/tests/testthat/test-neighborhood.R
/usr/lib64/R/library/igraph/tests/testthat/test-neighbors.R
/usr/lib64/R/library/igraph/tests/testthat/test-new-layout-api.R
/usr/lib64/R/library/igraph/tests/testthat/test-notable.R
/usr/lib64/R/library/igraph/tests/testthat/test-old-data-type.R
/usr/lib64/R/library/igraph/tests/testthat/test-operators.R
/usr/lib64/R/library/igraph/tests/testthat/test-operators3.R
/usr/lib64/R/library/igraph/tests/testthat/test-operators4.R
/usr/lib64/R/library/igraph/tests/testthat/test-optimal.community.R
/usr/lib64/R/library/igraph/tests/testthat/test-pajek.R
/usr/lib64/R/library/igraph/tests/testthat/test-plot.R
/usr/lib64/R/library/igraph/tests/testthat/test-print.R
/usr/lib64/R/library/igraph/tests/testthat/test-random_walk.R
/usr/lib64/R/library/igraph/tests/testthat/test-read_graph.R
/usr/lib64/R/library/igraph/tests/testthat/test-rewire.R
/usr/lib64/R/library/igraph/tests/testthat/test-sample.R
/usr/lib64/R/library/igraph/tests/testthat/test-sbm.game.R
/usr/lib64/R/library/igraph/tests/testthat/test-scan.R
/usr/lib64/R/library/igraph/tests/testthat/test-sdf.R
/usr/lib64/R/library/igraph/tests/testthat/test-serialize.R
/usr/lib64/R/library/igraph/tests/testthat/test-sgm.R
/usr/lib64/R/library/igraph/tests/testthat/test-sir.R
/usr/lib64/R/library/igraph/tests/testthat/test-sphere.R
/usr/lib64/R/library/igraph/tests/testthat/test-topology.R
/usr/lib64/R/library/igraph/tests/testthat/test-transitivity.R
/usr/lib64/R/library/igraph/tests/testthat/test-trees.R
/usr/lib64/R/library/igraph/tests/testthat/test-triangles.R
/usr/lib64/R/library/igraph/tests/testthat/test-unfold.tree.R
/usr/lib64/R/library/igraph/tests/testthat/test-utils-ensure.R
/usr/lib64/R/library/igraph/tests/testthat/test-version.R
/usr/lib64/R/library/igraph/tests/testthat/test-versions.R
/usr/lib64/R/library/igraph/tests/testthat/test-vs-es-printing.R
/usr/lib64/R/library/igraph/tests/testthat/test-vs-es-quirks.R
/usr/lib64/R/library/igraph/tests/testthat/test-vs-es.R
/usr/lib64/R/library/igraph/tests/testthat/test-vs-operators.R
/usr/lib64/R/library/igraph/tests/testthat/test-walktrap.community.R
/usr/lib64/R/library/igraph/tests/testthat/test-watts.strogatz.game.R
/usr/lib64/R/library/igraph/tests/testthat/test-weakref.R
/usr/lib64/R/library/igraph/tests/testthat/test-weighted_cliques.R
/usr/lib64/R/library/igraph/tests/testthat/zachary.graphml.gz
/usr/lib64/R/library/igraph/tkigraph_help/communities.html
/usr/lib64/R/library/igraph/tkigraph_help/index.html
/usr/lib64/R/library/igraph/tkigraph_help/style.css
/usr/lib64/R/library/igraph/tkigraph_help/tkigraph-main.gif

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/igraph/libs/igraph.so
/usr/lib64/R/library/igraph/libs/igraph.so.avx2
/usr/lib64/R/library/igraph/libs/igraph.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-igraph/16fd05e0c827f9372ff54c2a16b30353842a6df1
