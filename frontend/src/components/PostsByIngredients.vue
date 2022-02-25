<template>
  <div>
    <h2>Posts in #{{ $route.params.ingredients }}</h2>
    <PostList :posts="posts" v-if="posts" />
  </div>
</template>

<script>
import PostList from '../components/PostList.vue'
import gql from 'graphql-tag'


export default {
  name: 'postsByIngredients',
  components: {
    PostList,
  },
  data () {
    return {
      posts: null,
    }
  },
   async created () {
    const posts = await this.$apollo.query({
      query: gql`query ($ingredients: String!) {
        postsByIngredients(ingredients: $ingredients) {
          title
          subtitle
          publishDate
          published
          metaDescription
          slug
          author {
            user {
              username
              firstName
              lastName
            }
          }
          tags {
            name
          }
        }
      }`,
      variables: {
        tag: this.$route.params.ingredients,
      },
    })
    this.posts = posts.data.postsByIngredients
  },
}
</script>