#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-igraph
Version  : 1.2.6
Release  : 39
URL      : https://cran.r-project.org/src/contrib/igraph_1.2.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/igraph_1.2.6.tar.gz
Summary  : Network Analysis and Visualization
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: R-igraph-lib = %{version}-%{release}
Requires: R-magrittr
Requires: R-pkgconfig
BuildRequires : R-magrittr
BuildRequires : R-pkgconfig
BuildRequires : buildreq-R
BuildRequires : gmp-dev
BuildRequires : libxml2-dev
BuildRequires : xz-dev

%description
handle large graphs very well and provides functions for generating random
  and regular graphs, graph visualization, centrality methods and much more.

%package lib
Summary: lib components for the R-igraph package.
Group: Libraries

%description lib
lib components for the R-igraph package.


%prep
%setup -q -c -n igraph
cd %{_builddir}/igraph

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602175504

%install
export SOURCE_DATE_EPOCH=1602175504
rm -rf %{buildroot}
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library igraph
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library igraph
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library igraph
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc igraph || :


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
/usr/lib64/R/library/igraph/NAMESPACE
/usr/lib64/R/library/igraph/NEWS.md
/usr/lib64/R/library/igraph/R/igraph
/usr/lib64/R/library/igraph/R/igraph.rdb
/usr/lib64/R/library/igraph/R/igraph.rdx
/usr/lib64/R/library/igraph/README.md
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
/usr/lib64/R/library/igraph/tests/testthat/celegansneural.gml.gz
/usr/lib64/R/library/igraph/tests/testthat/dyad.census.R
/usr/lib64/R/library/igraph/tests/testthat/football.gml.gz
/usr/lib64/R/library/igraph/tests/testthat/helper.R
/usr/lib64/R/library/igraph/tests/testthat/power.gml.gz
/usr/lib64/R/library/igraph/tests/testthat/test-constructor-modifiers.R
/usr/lib64/R/library/igraph/tests/testthat/test-graph-ids.R
/usr/lib64/R/library/igraph/tests/testthat/test-index-es.R
/usr/lib64/R/library/igraph/tests/testthat/test-isomorphism.R
/usr/lib64/R/library/igraph/tests/testthat/test-make.R
/usr/lib64/R/library/igraph/tests/testthat/test-make_graph.R
/usr/lib64/R/library/igraph/tests/testthat/test-new-layout-api.R
/usr/lib64/R/library/igraph/tests/testthat/test-notable.R
/usr/lib64/R/library/igraph/tests/testthat/test-old-data-type.R
/usr/lib64/R/library/igraph/tests/testthat/test-random_walk.R
/usr/lib64/R/library/igraph/tests/testthat/test-version.R
/usr/lib64/R/library/igraph/tests/testthat/test-versions.R
/usr/lib64/R/library/igraph/tests/testthat/test-vs-es-printing.R
/usr/lib64/R/library/igraph/tests/testthat/test-vs-es-quirks.R
/usr/lib64/R/library/igraph/tests/testthat/test-vs-es.R
/usr/lib64/R/library/igraph/tests/testthat/test-vs-operators.R
/usr/lib64/R/library/igraph/tests/testthat/test-weakref.R
/usr/lib64/R/library/igraph/tests/testthat/test_add.edges.R
/usr/lib64/R/library/igraph/tests/testthat/test_add.vertices.R
/usr/lib64/R/library/igraph/tests/testthat/test_adjacency.spectral.embedding.R
/usr/lib64/R/library/igraph/tests/testthat/test_all.st.cuts.R
/usr/lib64/R/library/igraph/tests/testthat/test_alpha.centrality.R
/usr/lib64/R/library/igraph/tests/testthat/test_are.connected.R
/usr/lib64/R/library/igraph/tests/testthat/test_arpack.R
/usr/lib64/R/library/igraph/tests/testthat/test_articulation.points.R
/usr/lib64/R/library/igraph/tests/testthat/test_as.directed.R
/usr/lib64/R/library/igraph/tests/testthat/test_as.undirected.R
/usr/lib64/R/library/igraph/tests/testthat/test_assortativity.R
/usr/lib64/R/library/igraph/tests/testthat/test_attributes.R
/usr/lib64/R/library/igraph/tests/testthat/test_authority.score.R
/usr/lib64/R/library/igraph/tests/testthat/test_average.path.length.R
/usr/lib64/R/library/igraph/tests/testthat/test_ba.game.R
/usr/lib64/R/library/igraph/tests/testthat/test_betweenness.R
/usr/lib64/R/library/igraph/tests/testthat/test_biconnected.components.R
/usr/lib64/R/library/igraph/tests/testthat/test_bipartite.projection.R
/usr/lib64/R/library/igraph/tests/testthat/test_bipartite.random.game.R
/usr/lib64/R/library/igraph/tests/testthat/test_bonpow.R
/usr/lib64/R/library/igraph/tests/testthat/test_bug-1019624.R
/usr/lib64/R/library/igraph/tests/testthat/test_bug-1032819.R
/usr/lib64/R/library/igraph/tests/testthat/test_bug-1033045.R
/usr/lib64/R/library/igraph/tests/testthat/test_bug-1073705-indexing.R
/usr/lib64/R/library/igraph/tests/testthat/test_bug-1073800-clique.R
/usr/lib64/R/library/igraph/tests/testthat/test_canonical.permutation.R
/usr/lib64/R/library/igraph/tests/testthat/test_cliques.R
/usr/lib64/R/library/igraph/tests/testthat/test_closeness.R
/usr/lib64/R/library/igraph/tests/testthat/test_clusters.R
/usr/lib64/R/library/igraph/tests/testthat/test_communities.R
/usr/lib64/R/library/igraph/tests/testthat/test_constraint.R
/usr/lib64/R/library/igraph/tests/testthat/test_contract.vertices.R
/usr/lib64/R/library/igraph/tests/testthat/test_correlated.R
/usr/lib64/R/library/igraph/tests/testthat/test_count.multiple.R
/usr/lib64/R/library/igraph/tests/testthat/test_decompose.graph.R
/usr/lib64/R/library/igraph/tests/testthat/test_degree.R
/usr/lib64/R/library/igraph/tests/testthat/test_degree.sequence.game.R
/usr/lib64/R/library/igraph/tests/testthat/test_delete.edges.R
/usr/lib64/R/library/igraph/tests/testthat/test_delete.vertices.R
/usr/lib64/R/library/igraph/tests/testthat/test_diameter.R
/usr/lib64/R/library/igraph/tests/testthat/test_dimSelect.R
/usr/lib64/R/library/igraph/tests/testthat/test_dominator.tree.R
/usr/lib64/R/library/igraph/tests/testthat/test_dot.product.game.R
/usr/lib64/R/library/igraph/tests/testthat/test_dyad.census.R
/usr/lib64/R/library/igraph/tests/testthat/test_edge.betweenness.R
/usr/lib64/R/library/igraph/tests/testthat/test_edge.betweenness.community.R
/usr/lib64/R/library/igraph/tests/testthat/test_edge.connectivity.R
/usr/lib64/R/library/igraph/tests/testthat/test_edgenames.R
/usr/lib64/R/library/igraph/tests/testthat/test_evcent.R
/usr/lib64/R/library/igraph/tests/testthat/test_fartherst.nodes.R
/usr/lib64/R/library/igraph/tests/testthat/test_fastgreedy.community.R
/usr/lib64/R/library/igraph/tests/testthat/test_forestfire.R
/usr/lib64/R/library/igraph/tests/testthat/test_get.adjacency.R
/usr/lib64/R/library/igraph/tests/testthat/test_get.adjlist.R
/usr/lib64/R/library/igraph/tests/testthat/test_get.all.shortest.paths.R
/usr/lib64/R/library/igraph/tests/testthat/test_get.diameter.R
/usr/lib64/R/library/igraph/tests/testthat/test_get.edge.R
/usr/lib64/R/library/igraph/tests/testthat/test_get.edgelist.R
/usr/lib64/R/library/igraph/tests/testthat/test_get.incidence.R
/usr/lib64/R/library/igraph/tests/testthat/test_get.shortest.paths.R
/usr/lib64/R/library/igraph/tests/testthat/test_girth.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.adhesion.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.adjacency.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.adjlist.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.atlas.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.bfs.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.bipartite.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.complementer.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.compose.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.coreness.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.data.frame.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.de.bruijn.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.density.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.edgelist.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.eigen.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.formula.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.isoclass.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.kautz.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.knn.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.maxflow.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.mincut.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.subisomorphic.lad.R
/usr/lib64/R/library/igraph/tests/testthat/test_graph.subisomorphic.vf2.R
/usr/lib64/R/library/igraph/tests/testthat/test_graphNEL.R
/usr/lib64/R/library/igraph/tests/testthat/test_graphlets.R
/usr/lib64/R/library/igraph/tests/testthat/test_hrg.R
/usr/lib64/R/library/igraph/tests/testthat/test_hsbm.R
/usr/lib64/R/library/igraph/tests/testthat/test_igraph.options.R
/usr/lib64/R/library/igraph/tests/testthat/test_independent.vertex.sets.R
/usr/lib64/R/library/igraph/tests/testthat/test_indexing.R
/usr/lib64/R/library/igraph/tests/testthat/test_indexing2.R
/usr/lib64/R/library/igraph/tests/testthat/test_indexing3.R
/usr/lib64/R/library/igraph/tests/testthat/test_is.bipartite.R
/usr/lib64/R/library/igraph/tests/testthat/test_is.chordal.R
/usr/lib64/R/library/igraph/tests/testthat/test_iterators.R
/usr/lib64/R/library/igraph/tests/testthat/test_label.propagation.community.R
/usr/lib64/R/library/igraph/tests/testthat/test_laplacian.spectral.embedding.R
/usr/lib64/R/library/igraph/tests/testthat/test_largest.cliques.R
/usr/lib64/R/library/igraph/tests/testthat/test_largest.independent.vertex.sets.R
/usr/lib64/R/library/igraph/tests/testthat/test_layout.fr.R
/usr/lib64/R/library/igraph/tests/testthat/test_layout.kk.R
/usr/lib64/R/library/igraph/tests/testthat/test_layout.mds.R
/usr/lib64/R/library/igraph/tests/testthat/test_layout.merge.R
/usr/lib64/R/library/igraph/tests/testthat/test_leading.eigenvector.community.R
/usr/lib64/R/library/igraph/tests/testthat/test_maximal_cliques.R
/usr/lib64/R/library/igraph/tests/testthat/test_minimal.st.separators.R
/usr/lib64/R/library/igraph/tests/testthat/test_minimum.size.separators.R
/usr/lib64/R/library/igraph/tests/testthat/test_modularity_matrix.R
/usr/lib64/R/library/igraph/tests/testthat/test_motifs.R
/usr/lib64/R/library/igraph/tests/testthat/test_multilevel.community.R
/usr/lib64/R/library/igraph/tests/testthat/test_neighborhood.R
/usr/lib64/R/library/igraph/tests/testthat/test_neighbors.R
/usr/lib64/R/library/igraph/tests/testthat/test_operators.R
/usr/lib64/R/library/igraph/tests/testthat/test_operators3.R
/usr/lib64/R/library/igraph/tests/testthat/test_operators4.R
/usr/lib64/R/library/igraph/tests/testthat/test_optimal.community.R
/usr/lib64/R/library/igraph/tests/testthat/test_pajek.R
/usr/lib64/R/library/igraph/tests/testthat/test_print.R
/usr/lib64/R/library/igraph/tests/testthat/test_psumtree.R
/usr/lib64/R/library/igraph/tests/testthat/test_sample.R
/usr/lib64/R/library/igraph/tests/testthat/test_sbm.game.R
/usr/lib64/R/library/igraph/tests/testthat/test_scan.R
/usr/lib64/R/library/igraph/tests/testthat/test_sdf.R
/usr/lib64/R/library/igraph/tests/testthat/test_sgm.R
/usr/lib64/R/library/igraph/tests/testthat/test_sir.R
/usr/lib64/R/library/igraph/tests/testthat/test_sphere.R
/usr/lib64/R/library/igraph/tests/testthat/test_transitivity.R
/usr/lib64/R/library/igraph/tests/testthat/test_triangles.R
/usr/lib64/R/library/igraph/tests/testthat/test_unfold.tree.R
/usr/lib64/R/library/igraph/tests/testthat/test_walktrap.community.R
/usr/lib64/R/library/igraph/tests/testthat/test_watts.strogatz.game.R
/usr/lib64/R/library/igraph/tkigraph_help/communities.html
/usr/lib64/R/library/igraph/tkigraph_help/index.html
/usr/lib64/R/library/igraph/tkigraph_help/style.css
/usr/lib64/R/library/igraph/tkigraph_help/tkigraph-main.gif

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/igraph/libs/igraph.so
/usr/lib64/R/library/igraph/libs/igraph.so.avx2
/usr/lib64/R/library/igraph/libs/igraph.so.avx512
